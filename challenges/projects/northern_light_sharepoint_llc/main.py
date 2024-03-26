"""
Northern Light Sharepoint LLC -> File Comparitor

Copyright ©2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""
import os


def compare_files(file0: str, file1: str, output0: str, output1: str) -> None:
    """
    Compare two files and write the unique lines from each file to two separate output files.

    This function takes in four arguments: two input file paths and two output file paths.
    It reads the input files line by line, compares them, and writes the unique lines to the output files.
    The function uses sets to store the lines from each file. The difference between two sets in Python gives the elements
    present in the first set but not in the second.
    This is used to find the unique lines in each file. The unique lines are then written to the output files.

    Args:
        file0 (str): Path to the first input file.
        file1 (str): Path to the second input file.
        output0 (str): Path to the first output file.
        output1 (str): Path to the second output file.

    Returns:
        None

    Raises:
        IOError: An error occurred while processing the files.
    """
    # Check if input files exist and are accessible
    if not os.path.exists(file0) or not os.path.exists(file1):
        raise IOError("One or both input files do not exist or are not accessible.")

    try:
        # Open the input files and read the lines into sets
        with open(file0) as f0, open(file1) as f1:
            set1 = set(line for line in f0)
            set2 = set(line for line in f1)

        # Find the unique lines in each file
        out_0 = sorted(set1 - set2)
        out_1 = sorted(set2 - set1)

        # Write the unique lines to the output files
        with open(output0, 'w', newline='\n') as out0:
            out0.writelines(out_0)

        with open(output1, 'w', newline='\n') as out1:
            out1.writelines(out_1)
    except IOError as e:
        print(f"An error occurred while processing the files: {e}")


# Call the function with your file paths
compare_files('./data/input_0.csv', './data/input_1.csv', './data/output1.csv', './data/output2.csv')
