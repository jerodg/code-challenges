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
"""


def make_readable(seconds: int) -> str:
    """Convert seconds to a human-readable time format (HH:MM:SS).

    Parameters:
        seconds: A non-negative integer representing the total number of seconds.

    Returns:
        A string in the format HH:MM:SS where:
        - HH: hours padded to 2 digits (00-99)
        - MM: minutes padded to 2 digits (00-59)
        - SS: seconds padded to 2 digits (00-59)

    Example:
        >>> make_readable(0)
        "00:00:00"
        >>> make_readable(5)
        "00:00:05"
        >>> make_readable(60)
        "00:01:00"
        >>> make_readable(86399)
        "23:59:59"
        >>> make_readable(359999)
        "99:59:59"
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"