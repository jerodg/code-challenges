"""LeetCode 1922 Count Good Numbers.

This module implements a solution for LeetCode problem 1922: Count Good Numbers.
A digit string is considered good if the digits (0-indexed) at even indices are even (0, 2, 4, 6, 8)
and the digits at odd indices are prime (2, 3, 5, 7).
The solution calculates the count of good numbers of length n.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""


class Solution:
    """A class for solving the Count Good Numbers problem.

    This class provides a method to calculate the number of good digit strings
    of a given length, where a "good" digit string follows specific rules for
    digits at even and odd positions.
    """

    def countGoodNumbers(self, n: int) -> int:
        """Count the number of good strings of length n.

        A digit string is considered good if the digits (0-indexed) at even indices are even (0, 2, 4, 6, 8)
        and the digits at odd indices are prime (2, 3, 5, 7).

        For even indices, there are 5 possibilities (0, 2, 4, 6, 8).
        For odd indices, there are 4 possibilities (2, 3, 5, 7).

        The solution uses fast exponentiation to compute the result efficiently.

        Parameters:
            n: The length of the digit string.

        Returns:
            The number of good digit strings of length n, modulo 10^9 + 7.

        Example:
            >>> sol = Solution()
            >>> sol.countGoodNumbers(1)  # 1 digit, even position only: 5 options
            5
            >>> sol.countGoodNumbers(4)  # 5*4*5*4 = 400
            400
        """
        MOD = 10**9 + 7

        def expo(x: int, num: int) -> int:
            """Calculate x^num efficiently using fast exponentiation.

            This helper function implements binary exponentiation to compute
            x^num mod MOD efficiently with O(log n) time complexity.

            Parameters:
                x: The base number.
                num: The exponent.

            Returns:
                The result of x^num mod MOD.
            """
            if num == 0:
                return 1
            if num % 2 == 0:
                return expo(x**2 % MOD, num // 2)
            return x * expo(x, num - 1) % MOD

        # For a length n:
        # - Even positions: ceil(n/2) positions with 5 options each
        # - Odd positions: floor(n/2) positions with 4 options each
        # This can be calculated as 5^(n - n//2) * 4^(n//2) which simplifies to:
        # - If n is odd: 5^((n+1)/2) * 4^(n/2)
        # - If n is even: 5^(n/2) * 4^(n/2) = (5*4)^(n/2) = 20^(n/2)
        return 5 ** (n % 2) * expo(20, n // 2) % MOD
