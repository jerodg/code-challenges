"""HackerRank Validating UID Solution.

Provides a function to validate User Identification Numbers (UIDs)
based on a specific set of rules defined by a HackerRank challenge. It reads
a number of test cases, validates each UID, and prints the result.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""

import re


def validate_uid(uid: str) -> str:
    """Validates a UID based on HackerRank rules.

    Checks if the provided UID string meets the following criteria:
    1. Must contain at least 2 uppercase English alphabet characters.
    2. Must contain at least 3 digits (0-9).
    3. Must contain only alphanumeric characters (a-z, A-Z, 0-9).
    4. No character should repeat.
    5. Must be exactly 10 characters long.

    Args:
        uid: The User Identification Number string to validate.

    Returns:
        "Valid" if the UID meets all criteria, otherwise "Invalid".

    Examples:
        >>> validate_uid("B1CD102354")
        'Valid'
        >>> validate_uid("B1CDEF2354") # Needs 3 digits
        'Invalid'
        >>> validate_uid("b1cd102354") # Needs 2 uppercase
        'Invalid'
        >>> validate_uid("B1CD10235") # Needs 10 chars
        'Invalid'
        >>> validate_uid("B1CD10235!") # Needs alphanumeric only
        'Invalid'
        >>> validate_uid("B1CD102355") # Needs unique chars
        'Invalid'
        >>> validate_uid("ABCDEFGHIJ") # Needs 3 digits
        'Invalid'
        >>> validate_uid("1234567890") # Needs 2 uppercase
        'Invalid'
    """
    # Rule 5: UID must be exactly 10 characters long.
    if len(uid) != 10:
        return "Invalid"

    # Rule 3: UID must consist of only alphanumeric characters.
    # This check ensures no special characters are present.
    if not uid.isalnum():
        return "Invalid"

    # Rule 1: UID must have at least 2 uppercase letters.
    # Uses regex to find all occurrences of uppercase letters.
    if len(re.findall(r"[A-Z]", uid)) < 2:
        return "Invalid"

    # Rule 2: UID must have at least 3 digits.
    # Uses regex to find all occurrences of digits.
    if len(re.findall(r"\d", uid)) < 3:
        return "Invalid"

    # Rule 4: All characters in the UID must be unique.
    # Converts the string to a set to check for duplicate characters.
    # If the length of the set is not 10, duplicates exist.
    if len(set(uid)) != 10:
        return "Invalid"

    # If all rules pass, the UID is considered valid.
    return "Valid"


if __name__ == "__main__":
    # T represents the number of test cases (UIDs) to validate.
    T: int = int(input())
    # Loop through each test case.
    for _ in range(T):
        # Read the UID string from standard input for the current test case.
        uid_input: str = input()
        # Validate the UID and print the result ("Valid" or "Invalid").
        print(validate_uid(uid_input))