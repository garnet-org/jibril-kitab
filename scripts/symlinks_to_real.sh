#!/bin/bash
set -e

# Convert all symlinks in mitre/TA*/ directories to real files.
# This is needed for GitBook compatibility.

for ta_dir in mitre/TA*/; do
  for md in "$ta_dir"*.md; do
    if [ -L "$md" ]; then
      # If it's a symlink, replace it with a real copy.
      real_file=$(readlink -f "$md")
      rm "$md"
      cp "$real_file" "$md"
      echo "Converted symlink to real file: $md"
    fi
  done
done

echo "All symlinks have been converted to real files."
