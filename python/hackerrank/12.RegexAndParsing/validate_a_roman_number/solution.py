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

HackerRank solution for validating a Roman numeral.
"""

import re


def validate_roman_numeral(s: str) -> bool:
    """Validate whether a string is a valid Roman numeral between 1 and 3999.

    Uses a regular expression to validate the structure of Roman numerals.
    The pattern enforces correct character sequences and combinations
    according to Roman numeral rules.

    Parameters:
        s (str): The string to validate as a Roman numeral.

    Returns:
        bool: True if the string is a valid Roman numeral, False otherwise.

    Example:
        >>> validate_roman_numeral("CDXXI")
        True
        >>> validate_roman_numeral("MMMDCCCXCIX")
        True
        >>> validate_roman_numeral("IIIIIV")
        False
    """
    # Pattern explanation:
    # M{0,3} - 0 to 3 M's (thousands: 0-3000)
    # (CM|CD|D?C{0,3}) - hundreds: 900 (CM), 400 (CD), or 0-300 (C{0,3}) with optional 500 (D)
    # (XC|XL|L?X{0,3}) - tens: 90 (XC), 40 (XL), or 0-30 (X{0,3}) with optional 50 (L)
    # (IX|IV|V?I{0,3}) - units: 9 (IX), 4 (IV), or 0-3 (I{0,3}) with optional 5 (V)
    pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

    return bool(re.match(pattern, s))


# Read input and print result
print(validate_roman_numeral(input().strip()))
