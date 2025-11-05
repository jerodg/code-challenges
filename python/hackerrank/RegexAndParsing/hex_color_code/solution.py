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

HackerRank problem: Hex Color Code
"""

import re

CRE = re.compile(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b")


def main() -> None:
    """Extract and print valid hex color codes from CSS property values.

    This function processes CSS input, extracts all valid hex color codes, and prints them.
    Valid hex codes begin with '#' and consist of either 3 or 6 hexadecimal characters.
    Only hex codes that appear in property values (after colons) are captured.

    The function:
    1. Reads N lines of CSS input
    2. Extracts all CSS blocks (content within curly braces)
    3. Within each block, finds property values (content between ':' and ';')
    4. Extracts valid hex color codes from these values using the pre-compiled regex
    5. Prints each hex color on a separate line

    Returns:
        None: Results are printed to stdout

    Example:
        For input:
        ```
        2
        .class {
            color: #FFF;
            background-color: #ABC123;
        }
        ```
        Output will be:
        ```
        # FFF
        # ABC123
        ```
    """
    n = int(input().strip())
    css_code = "\n".join(input() for _ in range(n))

    # Find all CSS blocks (content between braces)
    css_blocks = re.findall(r"{[^}]*}", css_code, re.DOTALL)

    hex_colors = []
    for block in css_blocks:
        # Find all property declarations within each block
        properties = re.findall(r":(.*?);", block)
        for prop in properties:
            # Extract hex color codes from property values
            colors = re.findall(CRE, prop)
            hex_colors.extend(["#" + color for color in colors])

    # Print each hex color on a new line
    for color in hex_colors:
        print(color)


if __name__ == "__main__":
    main()
