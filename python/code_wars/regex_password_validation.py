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

Regex Password Validation

This module provides a regular expression pattern for validating passwords
according to specific security criteria:
- At least six characters long
- Contains at least one lowercase letter
- Contains at least one uppercase letter
- Contains at least one digit
- Only contains alphanumeric characters
"""

import re

# Regex pattern that validates password criteria
regex = re.compile(
    r'^'  # ^ - Start of the string
    r'(?=.*[a-z])'  # (?=.*[a-z]) - At least one lowercase letter
    r'(?=.*[A-Z])'  # (?=.*[A-Z]) - At least one uppercase letter
    r'(?=.*\d)'  # (?=.*\d) - At least one digit
    r'[a-zA-Z0-9]{6,}'  # [a-zA-Z0-9]{6,} - At least six alphanumeric characters
    r'$'  # $ - End of the string
)
