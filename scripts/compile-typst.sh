#!/usr/bin/env bash

set -euo pipefail

mode="${1:-light}"

case "$mode" in
  light) theme_flag=""; out="main.pdf" ;;
  dark) theme_flag="--input theme=dark"; out="main-dark.pdf" ;;
  all)
    "$0" light
    "$0" dark
    exit 0
    ;;
  *)
    echo "Usage: $0 [light|dark|all]"
    exit 1
    ;;
esac

echo "Compiling Typst ($mode) -> $out"
typst compile --root . --font-path assets/ $theme_flag book/main.typ "$out"

pages="$(typst eval --root . --font-path assets/ $theme_flag 'query(<end>).first().value' --in book/main.typ)"
if [ "$pages" -gt 25 ]; then
  echo "::error::$out has $pages pages (max 25)"
  exit 1
fi

echo "Typst compilation OK ($pages pages)"
