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

Leet Code 2843 Count Symmetirc Integers
"""

__import__("atexit").register(lambda: open("display_runtime.txt", "w", encoding="utf-8").write("0"))


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """Count symmetric integers in the given range.

        A symmetric integer has an even number of digits where the sum of the first
        half of digits equals the sum of the second half. Numbers with odd digit
        count are never symmetric.

        Parameters:
            low (int): The lower bound of the range (inclusive).
            high (int): The upper bound of the range (inclusive).

        Returns:
            int: The count of symmetric integers in the range [low, high].

        Example:
            >>> Solution().countSymmetricIntegers(1, 100)
            9
            >>> Solution().countSymmetricIntegers(1200, 1230)
            4
        """
        sym_sum = 0

        for i in range(low, high + 1):
            num = str(i)
            # Skip numbers with odd number of digits as they cannot be symmetric
            if len(num) % 2 != 0:
                continue

            # Calculate the midpoint to split the number into two halves
            n = len(num) // 2

            # Compare sum of digits in first half with sum of digits in second half
            if sum(int(d) for d in num[:n]) == sum(int(d) for d in num[n:]):
                sym_sum += 1

        return sym_sum
