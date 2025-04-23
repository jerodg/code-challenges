"""LeetCode 1399. Count Largest Group Solution.

Implements a solution to count the number of groups with the largest size,
where numbers from 1 to n are grouped by the sum of their digits using
dynamic programming.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""


class Solution:
    """Solves the LeetCode 1399 problem: Count Largest Group.

    This class provides a method to count the number of groups with the
    largest size, where numbers from 1 to n are grouped by the sum of
    their digits using a dynamic programming approach for efficiency.
    """

    def countLargestGroup(self, n: int) -> int:
        """Counts the number of groups with the largest size using DP.

        Numbers from 1 to n are grouped based on the sum of their digits.
        This method calculates the size of each group (how many numbers share
        the same digit sum) and determines the maximum size achieved by any group.
        It then returns the count of groups that have this maximum size.

        It uses dynamic programming to calculate digit sums efficiently.
        `total_sum[i]` stores the digit sum of `i`. The digit sum of `i` is
        calculated as `(i % 10) + total_sum[i // 10]`.

        Args:
            n: The upper limit integer (inclusive, 1 <= n <= 10^4). Numbers
               from 1 to n will be considered for grouping.

        Returns:
            The number of groups having the largest size.

        Examples:
            >>> sol = Solution()
            >>> sol.countLargestGroup(13)
            4
            >>> sol.countLargestGroup(2)
            2
            >>> sol.countLargestGroup(24)
            5
        """
        # category stores the count of numbers for each possible digit sum.
        # The maximum possible digit sum for n <= 10000 is 9+9+9+9 = 36.
        # Index 0 is unused, indices 1-36 store counts for sums 1-36.
        category: list[int] = [0] * 37
        # total_sum stores the digit sum for each number from 0 to n.
        # total_sum[i] will hold the sum of digits of i.
        total_sum: list[int] = [0] * (n + 1)

        # Iterate through each number from 1 to n (inclusive).
        for i in range(1, n + 1):
            # Calculate the digit sum (sc) for the current number 'i' using DP.
            # The sum of digits of 'i' is the last digit (i % 10) plus
            # the sum of digits of the remaining number (i // 10).
            # The sum for i // 10 is already computed and stored in total_sum.
            sc: int = i % 10 + total_sum[i // 10]
            # Store the calculated digit sum for 'i' for future use.
            total_sum[i] = sc
            # Increment the count for the group corresponding to this digit sum 'sc'.
            category[sc] += 1

        # Find the maximum size among all groups (excluding sum 0).
        # max(category) finds the largest count in the category list.
        # category.count(...) counts how many times this maximum size appears.
        # Handles the case where category might be all zeros if n=0 (though constraints say n>=1).
        max_size = max(category)
        # Return 0 if max_size is 0 (only possible if n=0, which is outside constraints)
        # otherwise count occurrences of max_size.
        return category.count(max_size) if max_size > 0 else 0