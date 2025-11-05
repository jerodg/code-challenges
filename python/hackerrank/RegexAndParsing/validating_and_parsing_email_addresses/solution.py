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

HackerRank challenge: Validating and Parsing Email Addresses
"""

import email.utils
import re


def is_valid_email(email_addr: str) -> bool:
    """Validate if an email address meets the specified criteria.

    Parameters:
        email_addr (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.

    Example:
        >>> is_valid_email("dexter@hotmail.com")
        True
        >>> is_valid_email("virus!@variable.:p")
        False
    """
    # Pattern matches: username starts with a letter, followed by alphanumeric chars, -, ., or _,
    # then @, domain with only letters, period, and extension with 1-3 letters
    pattern = r"^[A-Za-z][A-Za-z0-9_\.\-]*@[A-Za-z]+\.[A-Za-z]{1,3}$"
    return bool(re.match(pattern, email_addr))


def main() -> None:
    """Process input and print valid email addresses with their names."""
    n = int(input())
    for _ in range(n):
        line = input()
        name, email_addr = email.utils.parseaddr(line)

        if is_valid_email(email_addr):
            print(email.utils.formataddr((name, email_addr)))


if __name__ == "__main__":
    main()
