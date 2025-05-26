#!/bin/bash
set -e

# Convert real files in mitre/TA*/ directories back to symlinks.
# This restores the symlink structure for efficient editing.

for ta_dir in mitre/TA*/; do
  for md in "$ta_dir"*.md; do
    # Skip if it's already a symlink.
    if [ -L "$md" ]; then
      continue
    fi

    # Only process real files.
    if [ -f "$md" ]; then
      filename=$(basename "$md")

      # Determine the canonical location based on filename pattern.
      if [[ "$filename" =~ ^TA[0-9]+\.md$ ]]; then
        # It's a tactic file (TA####.md).
        canonical="../tactics/$filename"
        canonical_full="mitre/tactics/$filename"
      elif [[ "$filename" =~ ^T[0-9]+(\.[0-9]+)?\.md$ ]]; then
        # It's a technique file (T####.md or T####.###.md).
        canonical="../techniques/$filename"
        canonical_full="mitre/techniques/$filename"
      else
        echo "Warning: Unknown file pattern: $md"
        continue
      fi

      # Check if the canonical file exists.
      if [ -f "$canonical_full" ]; then
        # Replace the real file with a symlink.
        rm "$md"
        ln -s "$canonical" "$md"
        echo "Converted real file to symlink: $md -> $canonical"
      else
        echo "Warning: Canonical file not found for $md (expected at $canonical_full)"
      fi
    fi
  done
done

echo "All real files have been converted to symlinks."
