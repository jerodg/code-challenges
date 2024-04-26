"""
Module for printing the square of each number in a range.

This module provides a solution for printing the square of each number in a range from 0 to a given number `n`.
The solution is implemented in the main function. This function takes an integer `n` as input and prints the square of each number in the range.

Example:
    >>> main(5)
    0
    1
    4
    9
    16

This module requires Python 3.12 or later.

Author:
    Jerod Gawne (https://github.com/jerodg)

Date:
    2024.1
"""


def main(n: int) -> None:
    """
    This function prints the square of each number in a range.

    Args:
        n (int): The upper limit of the range.

    Returns:
        None: The function prints the square of each number in the range and does not return a value.

    Raises:
        ValueError: If `n` is not an integer.

    Example:
        >>> main(5)
        0
        1
        4
        9
        16

        >>> main(3)
        0
        1
        4

        >>> main(1)
        0

        >>> main(0)
        # No output

        >>> main(-1)
        # No output
    """
    if not isinstance(n, int):
        raise ValueError('`n` must be an integer.')

    # Print the square of each number in the range
    [print(i**2) for i in range(n)]


if __name__ == '__main__':
    n = int(input())
    main(n)
