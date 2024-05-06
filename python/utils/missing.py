import os
import re

DRE = re.compile(r'(\d+)')

def find_leet_code_dirs(path):
    leet_code_dirs = []
    all_files = set()
    ignore_names = {'__init__', '__pycache__'}

    # Walk through each directory in the given path
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ignore_names]  # ignore directories in ignore_names
        if 'leet_code' in dirs:
            # Get the parent directory name
            language = os.path.split(root)[-1]
            # Get the unique file names in the 'leet_code' directory
            file_names = {
                os.path.splitext(file)[0]
                for file in os.listdir(os.path.join(root, 'leet_code'))
                if os.path.splitext(file)[0] not in ignore_names
            }
            # Add the file names to the set of all files
            all_files.update(file_names)
            # Count the unique file names
            file_count = len(file_names)
            leet_code_dirs.append((language, file_count))

    # Remove '.ws' from the end of filenames in all_files
    all_files = {file.rstrip('.ws') if file.endswith('.ws') else file for file in all_files}

    # Check that there aren't any file names with more than one extension
    for file in all_files:
        if file.count('.') > 1:
            print(f"Error: {file} has more than one extension")

    return leet_code_dirs, list(all_files)


if __name__ == '__main__':
    leet_code_dirs, all_files = find_leet_code_dirs('/devdrive/projects/code-challenges')
    print(*leet_code_dirs, sep='\n')
    af = sorted(all_files, key=lambda _: [int(s) if s.isdigit() else s.lower() for s in re.split(DRE, _)])
    print("All unique files across all 'leet_code' directories:", af)
