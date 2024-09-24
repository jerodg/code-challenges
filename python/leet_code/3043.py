"""Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""
from json import loads
from sys import stdin


class Solution:
    """A class to solve the problem of finding the longest common prefix in two lists of integers.

    This class provides a method to determine the longest common prefix between two lists of integers
    by checking the prefixes of each integer in the lists.
    """

    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        """Calculate the longest common prefix length between two lists of integers.

        This function uses a set to store all prefixes of integers from the first list. It then iterates
        through the second list to find the longest common prefix by checking if any prefix of the integers
        in the second list exists in the set.

        Parameters:
            arr1 (list[int]): The first list of integers.
            arr2 (list[int]): The second list of integers.

        Returns:
            int: The length of the longest common prefix found between the two lists.

        Example:
            >>> solution = Solution()
            >>> solution.longestCommonPrefix([123, 456], [1234, 567])
            3
        """
        # Use a set to store all prefixes of integers from the first list
        flag_s = set()

        for i in arr1:
            while i:
                # Add each prefix of the integer to the set
                flag_s.add(i)
                i //= 10

        ans = 0
        for i in arr2:
            while i:
                # Check if the prefix exists in the set
                if i in flag_s:
                    break
                i //= 10
            if i:
                # Update the answer with the length of the longest common prefix found
                ans = max(ans, len(str(i)))

        return ans


with open("user.out", "w") as f:
    # Read JSON input from standard input
    inputs = map(loads, stdin)
    i = 0
    args = []
    for a in inputs:
        i += 1
        args.append(a)
        # Process pairs of inputs
        if i & 1:
            continue
        # Calculate the longest common prefix and write the result to the output file
        print(str(Solution().longestCommonPrefix(*args)).replace(" ", ""), file=f)
        args = []

exit(0)