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

CodeWars String Incrementer
"""

import string


def increment_string(strng: str) -> str:
    """Increment a string by the number at its end.

    If the string ends with a number, increment that number by 1.
    If the string does not end with a number, append '1'.
    Preserves leading zeros in the number.

    Parameters:
        strng: The input string to be incremented.

    Returns:
        The incremented string.

    Examples:
        >>> increment_string("foo")
        'foo1'
        >>> increment_string("foobar23")
        'foobar24'
        >>> increment_string("foo0042")
        'foo0043'
        >>> increment_string("foo9")
        'foo10'
        >>> increment_string("foo099")
        'foo100'
    """
    # Find where the digits start (if any)
    head = strng.rstrip(string.digits)
    tail = strng[len(head) :]

    # If no digits were found, append '1'
    if not tail:
        return strng + "1"

    # Get the length of the numeric part for zero padding
    num_len = len(tail)

    # Increment the number and format it to preserve leading zeros
    new_tail = str(int(tail) + 1).zfill(num_len)

    return head + new_tail
