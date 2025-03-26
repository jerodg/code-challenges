"""Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

Password Validator
"""


def password(string: str) -> bool:
    """Validate a password based on the following rules.

    The function checks if a password meets security requirements by verifying:
    - At least 1 uppercase letter
    - At least 1 lowercase letter
    - At least 1 number
    - At least 8 characters long

    Parameters:
        string (str): The password to validate

    Returns:
        bool: True if the password meets all requirements, False otherwise

    Examples:
        >>> password('Abcd1234')
        True
        >>> password('Abcd123')
        False
        >>> password('abcd1234')
        False
        >>> password('ABCD1234')
        False
    """
    # Early return if the password is too short
    if len(string) < 8:
        return False

    # Track whether requirements are met using boolean flags
    has_uppercase = has_lowercase = has_number = False

    # Single pass through the password to check all character requirements
    for char in string:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_number = True

    # Only return True if all three character type requirements are met
    return has_uppercase and has_lowercase and has_number
