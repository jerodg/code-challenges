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

re.findall() & re.finditer()
"""

import re


def find_vowel_substrings(s: str) -> None:
    """Find and print vowel substrings that meet specific conditions.

    Locates all substrings that:
    1. Consist only of vowels
    2. Have 2 or more vowels
    3. Are located between two consonants

    Parameters:
        s (str): The input string to search within

    Returns:
        None: Results are printed to standard output

    Example:
        >>> find_vowel_substrings('rabcdeefgyYhFjkIoomnpOeorteeeeet')
        ee
        Ioo
        Oeo
        eeeee
    """
    # Define character classes for pattern matching
    consonants = r'[qwrtypsdfghjklzxcvbnm]'
    vowels = r'[aeiou]'

    # Construct regex pattern with lookaround assertions to find vowel sequences
    # between consonants without including the consonants in the match
    pattern = f'(?<={consonants})({vowels}{{2,}})(?={consonants})'

    # Find all non-overlapping matches in the string, ignoring case
    matches = re.findall(pattern, s, re.IGNORECASE)

    # Output results or -1 if no matches found
    if matches:
        for match in matches:
            print(match)
    else:
        print(-1)


# Process input when script is run directly
if __name__ == '__main__':
    s = input().strip()
    find_vowel_substrings(s)
