#!/usr/bin/env bash
#
# Commit the given paths and push to main, retrying against concurrent pushes.
#
# Usage: commit-and-push.sh "<commit message>" <path> [<path> ...]
#        commit-and-push.sh "<commit message>" --paths-from <file>
#
# On a rejected push the correct resolution is always "keep what this job just
# generated". Rather than rebasing (which dies on modify/delete conflicts, the
# way run 29826067399 did), we set the regenerated paths aside, reset onto
# whatever main looks like now, and lay them back on top. That overlay cannot
# conflict, and it never removes a file another job added in the meantime.
#
# Pass the narrowest paths you can. Handing over a whole directory means this
# job's copy of every file in it wins, which would revert a concurrent job's
# edit to a file this one did not actually regenerate. --paths-from reads a
# newline-delimited list, for when that list is long or computed.
set -euo pipefail

MESSAGE="$1"
shift

if [ "${1:-}" = "--paths-from" ]; then
  [ -f "$2" ] || { echo "Path list $2 does not exist." >&2; exit 1; }
  mapfile -t PATHS < <(grep -v '^[[:space:]]*$' "$2")
else
  PATHS=("$@")
fi

if [ ${#PATHS[@]} -eq 0 ]; then
  echo "No paths to commit"
  exit 0
fi
MAX_ATTEMPTS=${PUSH_MAX_ATTEMPTS:-5}

git config --local user.email "noreply@github.com"
git config --local user.name "github-actions[bot]"

STAGING=$(mktemp -d)
trap 'rm -rf "$STAGING"' EXIT

for attempt in $(seq 1 "$MAX_ATTEMPTS"); do
  rm -rf "${STAGING:?}"/*

  for path in "${PATHS[@]}"; do
    if [ -e "$path" ]; then
      mkdir -p "$STAGING/$(dirname "$path")"
      cp -R "$path" "$STAGING/$path"
    fi
  done

  git fetch origin main
  git reset --hard origin/main

  for path in "${PATHS[@]}"; do
    if [ -e "$STAGING/$path" ]; then
      mkdir -p "$(dirname "$path")"
      cp -RT "$STAGING/$path" "$path"
    fi
  done

  git add -A -- "${PATHS[@]}"
  if git diff --cached --quiet; then
    echo "No changes to commit"
    exit 0
  fi

  git commit -m "$MESSAGE"
  if git push origin HEAD:main; then
    echo "Pushed on attempt ${attempt}/${MAX_ATTEMPTS}."
    exit 0
  fi

  backoff=$(( attempt * 5 + RANDOM % 10 ))
  echo "Push rejected on attempt ${attempt}/${MAX_ATTEMPTS}; retrying in ${backoff}s."
  sleep "$backoff"
done

echo "Unable to push after ${MAX_ATTEMPTS} attempts." >&2
exit 1
