#!/bin/bash

SOURCE_FILE="$1"
PATTERN="$2"

pdfgrep "${PATTERN}"  "${SOURCE_FILE}" -n -i | \
sed -r 's/[:]+/: /g' | \
grep -w -i "${PATTERN}" | \
cut -f1 -d":" | \
uniq