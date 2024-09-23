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
import collections


class Solution:
    """A class to solve the problem of minimizing extra characters in a string.

    This class provides a method to determine the minimum number of extra characters
    needed to form a string using a given dictionary of words.
    """

    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        """Calculate the minimum number of extra characters needed to form the string `s`.

        This function uses dynamic programming to find the minimum number of extra characters
        required to form the string `s` using the words in the provided dictionary. It iterates
        through the string and checks for possible word matches from the dictionary, updating
        the dynamic programming table accordingly.

        Parameters:
            s (str): The input string to be formed.
            dictionary (list[str]): A list of words that can be used to form the string `s`.

        Returns:
            int: The minimum number of extra characters needed to form the string `s`.

        Example:
            >>> solution = Solution()
            >>> solution.minExtraChar("leetcode", ["leet", "code"])
            0
        """
        # Initialize the shortest word length to infinity
        short = float('inf')
        # Create a dictionary to store words by their last character
        book = collections.defaultdict(list)
        for w in dictionary:
            # Update the shortest word length
            short = min(short, len(w))
            # Append the word to the list of words ending with the same character
            book[w[-1]].append(w)

        # Initialize the dynamic programming table with the first `short` values
        dp = [i for i in range(short)]
        for i in range(short, len(s) + 1):
            # Start with the assumption that the current character is an extra character
            res = dp[i - 1] + 1
            for w in book[s[i - 1]]:
                # Skip words longer than the current substring
                if len(w) > i:
                    continue
                # If the word matches the end of the current substring, update the result
                if w == s[i - len(w):i]:
                    res = min(res, dp[i - len(w)])

            # Append the result to the dynamic programming table
            dp.append(res)

        # Return the minimum number of extra characters needed
        return dp[-1]