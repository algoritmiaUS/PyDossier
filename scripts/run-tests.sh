#!/usr/bin/env bash

set -euo pipefail

shopt -s nullglob
[ $# -gt 0 ] || set -- tests/unit/*.py tests/stress/*.py

logs="$(mktemp -d)"
trap 'rm -rf "$logs"' EXIT

run() {
  local out="$logs/${1//\//-}"
  local module="${1%.py}"
  PYTHONDONTWRITEBYTECODE=1 timeout 60 python3 -m "${module//\//.}" >"$out.log" 2>&1 || touch "$out.failed"
}

for t in "$@"; do
  while [ "$(jobs -rp | wc -l)" -ge "$(nproc)" ]; do wait -n; done
  run "$t" &
done
wait

failed=0
for t in "$@"; do
  out="$logs/${t//\//-}"
  echo "::group::Running $t"
  cat "$out.log"
  echo "::endgroup::"
  if [ -e "$out.failed" ]; then
    echo "::error file=$t::$t failed"
    failed=1
  fi
done

exit $failed
