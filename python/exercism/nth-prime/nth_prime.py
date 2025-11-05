"""Exercism Nth Prime

Given a number n, determine what the nth prime is.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""


def prime(number: int) -> int:
    """Find the nth prime number.

    This function iterates through integers starting from 2, checking each for primality
    until the nth prime is found. It uses an efficient primality test to handle large n
    without unnecessary computations.

    Args:
        number: The position of the prime to find, must be >= 1.

    Returns:
        The nth prime number.

    Raises:
        ValueError: If number is less than 1, as there is no zeroth prime.

    Example:
        >>> prime(1)
        2
        >>> prime(6)
        13
    """
    if number < 1:
        raise ValueError("there is no zeroth prime")

    # Initialize count of primes found and starting candidate to avoid negatives.
    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == number:
                return candidate
        candidate += 1


def is_prime(n: int) -> bool:
    """Check if a number is prime.

    This function uses trial division optimized for efficiency, skipping even numbers
    after 2 and checking divisors in increments of 6 to reduce iterations for larger n.

    Args:
        n: The number to check for primality.

    Returns:
        True if n is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # Start from 5 and increment by 6 to check only potential divisors, improving performance.
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
