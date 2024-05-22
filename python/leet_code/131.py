"""
Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
"""

"""
Package leet_code

This module contains the Solution class which is used to solve the problem of partitioning a string 
into all possible palindrome substrings.

The Solution class has a constructor and a method named partition. The constructor initializes an 
empty dictionary to store intermediate results for memoization. The partition method takes a string 
as input and returns a list of all possible palindrome partitioning of the input string.
"""


class Solution:
    """
    The Solution class is used to solve the problem of partitioning a string into all possible
    palindrome substrings.

    Attributes:
        ans (dict): a dictionary to store intermediate results for memoization.
    """

    def __init__(self):
        """
        The constructor for Solution class. Initializes an empty dictionary to store intermediate
        results for memoization.
        """
        self.ans = {}

    def partition(self, s: str) -> list[list[str]]:
        """
        The partition method takes a string as input and returns a list of all possible palindrome
        partitioning of the input string.

        Parameters:
            s (str): the input string to be partitioned.

        Returns:
            list[list[str]]: a list of all possible palindrome partitioning of the input string.

        This method uses a recursive approach to solve the problem. It checks if the current string
        is already computed and stored in the ans dictionary. If not, it computes the result by
        partitioning the string into all possible substrings and checking if they are palindromes.
        The results are then stored in the ans dictionary for future use.
        """

        # Check if the result for the current string is already computed and stored in the ans dictionary
        if s in self.ans:
            return self.ans[s]

        # If the string is empty, the result is an empty list
        if len(s) == 0:
            result = [[]]
        # If the string has only one character, the result is the string itself
        elif len(s) == 1:
            result = [[s]]
        else:
            result = []
            # Partition the string into all possible substrings
            for i in range(1, len(s) + 1):
                left = []
                # Check if the substring is a palindrome
                if s[:i] == "".join(reversed(s[:i])):
                    left.append([s[:i]])

                # Recursively call the partition method for the remaining part of the string
                right = self.partition(s[i:])

                # Combine the palindrome substring with the result of the recursive call
                for l in left:
                    for r in right:
                        result.append(l + r)

        # Store the result in the ans dictionary for future use
        self.ans[s] = result
        return result
