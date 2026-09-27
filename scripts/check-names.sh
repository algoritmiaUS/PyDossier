#!/usr/bin/env bash

set -euo pipefail

failed=0
while IFS= read -r path; do
  IFS=/ read -ra parts <<<"$path"
  for part in "${parts[@]}"; do
    [[ $part == .* || $part =~ ^(README|LICENSE|AGENTS|CONTRIBUTE)(\.md)?$ ]] && continue
    if [[ ! ${part%%.*} =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
      echo "::error::kebab-case violation: $path ('$part')"
      failed=1
      break
    fi
  done
done < <(git ls-files)

[ $failed -eq 0 ] && echo "All names are kebab-case"
exit $failed
