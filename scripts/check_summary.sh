#!/bin/bash

# This script checks for:
# 1. Markdown files that are not referenced in SUMMARY.md.
# 2. Broken links in SUMMARY.md (links to non-existent files).

# Exit on error, undefined variables, and propagate pipe failures.
set -euo pipefail

echo "=== DOCUMENTATION INTEGRITY CHECK ==="
echo

# Initialize counters and arrays
missing_references=0
broken_links=0
missing_files=()
broken_link_files=()

# Find all markdown files and check if they're referenced in SUMMARY.md.
echo "Checking for unreferenced markdown files..."
while read -r markdown_file; do
	filename=$(basename "$markdown_file")
	# Skip SUMMARY.md itself
	if [[ "$markdown_file" == "./SUMMARY.md" ]]; then
		continue
	fi
	if ! grep -q "$filename" SUMMARY.md; then
		missing_files+=("$markdown_file")
		missing_references=$((missing_references + 1))
	fi
done < <(find . -name "*.md" -type f)

# Check for broken links in SUMMARY.md.
echo "Checking for broken links in SUMMARY.md..."
while read -r file; do
	# Remove leading/trailing whitespace
	file=$(echo "$file" | xargs)
	if [[ -n "$file" ]] && ! [ -f "$file" ]; then
		broken_link_files+=("$file")
		broken_links=$((broken_links + 1))
	fi
done < <(grep -o '\[.*\](.*\.md)' SUMMARY.md | sed -E 's/\[(.*)\]\((.*)\)/\2/')

# Display results.
echo
echo "=== RESULTS ==="
echo

# Display unreferenced markdown files.
if [ ${#missing_files[@]} -gt 0 ]; then
	echo "Unreferenced markdown files:"
	for file in "${missing_files[@]}"; do
		echo "  - $file"
	done
	echo
else
	echo "All markdown files are referenced in SUMMARY.md"
	echo
fi

# Display broken links.
if [ ${#broken_link_files[@]} -gt 0 ]; then
	echo "Broken links in SUMMARY.md:"
	for file in "${broken_link_files[@]}"; do
		echo "  - $file"
	done
	echo
else
	echo "No broken links found in SUMMARY.md"
	echo
fi

# Summary.
echo "=== SUMMARY ==="
echo "Found $missing_references unreferenced markdown files"
echo "Found $broken_links broken links in SUMMARY.md"

# Exit with error code if issues were found.
if [ $missing_references -gt 0 ] || [ $broken_links -gt 0 ]; then
	exit 1
fi
