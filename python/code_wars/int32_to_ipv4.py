"""CodeWars int32 to IPv4.

This module provides a function to convert an unsigned 32-bit integer into its
IPv4 address representation. The function uses bitwise operations to extract
each octet of the IP address and formats them into the standard dotted-decimal
notation.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""

def int32_to_ipv4(n: int) -> str:
    """Convert an unsigned 32-bit integer to an IPv4 address.

    This function takes a 32-bit integer and converts it into its corresponding
    IPv4 address in dotted-decimal notation. The conversion is performed by
    extracting each of the four octets using bitwise operations and formatting
    them as a string.

    Parameters:
        n (int): The unsigned 32-bit integer to convert.

    Returns:
        str: The IPv4 address in dotted-decimal notation.

    Example:
        >>> int32_to_ipv4(2149583361)
        '128.32.10.1'
        >>> int32_to_ipv4(32)
        '0.0.0.32'
        >>> int32_to_ipv4(0)
        '0.0.0.0'

    Notes:
        - The input integer is assumed to be within the range of a 32-bit unsigned
          integer (0 to 2^32 - 1).
        - The function does not validate the input range; it is the caller's
          responsibility to ensure the input is valid.
    """
    # Use bitwise operations to extract each octet of the IPv4 address.
    # The range (3, -1, -1) ensures the octets are processed from most significant
    # to least significant, matching the order of an IPv4 address.
    return ".".join(str((n >> (8 * i)) & 0xFF) for i in range(3, -1, -1))
