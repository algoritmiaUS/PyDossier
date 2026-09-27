#!/usr/bin/env bash

set -euo pipefail

shopt -s globstar nullglob
files=(content/**/*.py tests/**/*.py)

if [ ${#files[@]} -eq 0 ]; then
  echo "No Python files found"
  exit 0
fi

failed=0
for f in "${files[@]}"; do
  echo "::group::Checking $f"
  python3 -c 'import ast, sys; ast.parse(open(sys.argv[1]).read(), sys.argv[1])' "$f" || failed=1
  echo "::endgroup::"
done

exit $failed
