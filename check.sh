#!/bin/bash

# Find all directories containing "leet_code" folder
roots=()
for dir in */; do
    if [ -d "${dir}leet_code" ]; then
        roots+=("${dir%/}")
    fi
done

if [ ${#roots[@]} -eq 0 ]; then
    echo "No directories containing 'leet_code' folder found."
    exit 1
fi

# Create associative array to store all unique numeric filenames
declare -A all_files
# Create associative array to track which roots are missing which files
declare -A missing_files

# First pass: collect all numeric filenames
for root in "${roots[@]}"; do
    while IFS= read -r file; do
        # Extract basename without extension
        base=$(basename "$file")
        filename="${base%.*}"
        # Check if filename contains only digits
        if [[ $filename =~ ^[0-9]+$ ]]; then
            all_files[$filename]=1
        fi
    done < <(find "${root}/leet_code" -type f 2>/dev/null)
done

# Second pass: check which files are missing from each root
for filename in "${!all_files[@]}"; do
    missing=""
    for root in "${roots[@]}"; do
        # Check if any file with this numeric base exists (regardless of extension)
        if ! ls "${root}/leet_code/${filename}".* >/dev/null 2>&1; then
            if [ -z "$missing" ]; then
                missing="$root"
            else
                missing="$missing, $root"
            fi
        fi
    done
    if [ ! -z "$missing" ]; then
        missing_files[$filename]="$missing"
    fi
done

# Output results
if [ ${#missing_files[@]} -eq 0 ]; then
    echo "All roots contain the same numeric files."
else
    echo "Missing files by root:"
    echo "----------------------"
    # Sort the filenames numerically
    while IFS= read -r filename; do
        if [ -n "${missing_files[$filename]}" ]; then
            echo "File $filename missing from: ${missing_files[$filename]}"
        fi
    done < <(printf "%s\n" "${!missing_files[@]}" | sort -n)
fi
