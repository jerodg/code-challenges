"""leet_code/1915.py

This module contains a solution for finding the number of wonderful substrings in a given word.
A wonderful string is a string where at most one letter appears an odd number of times.

The solution uses bitwise operations and a dictionary to keep track of the frequency of each character in the word.

Classes:
    Solution: This class contains a method to find the number of wonderful substrings in a word.
"""

from collections import defaultdict


class Solution:
    """A class used to find the number of wonderful substrings in a word.

    Methods:
        wonderfulSubstrings: Finds the number of wonderful substrings in a word.
    """

    def wonderfulSubstrings(self, word: str) -> int:
        """Finds the number of wonderful substrings in a word.

        Args:
            word (str): The word in which to find the number of wonderful substrings.

        Returns:
            int: The number of wonderful substrings in the word.

        This function does not handle errors explicitly. If the input is not a string, Python's built-in error handling will raise an exception.
        """

        # Initialize a dictionary to map each character to a unique bit
        tmp = defaultdict(int)
        for i in range(ord('a'), ord('j') + 1):
            tmp[chr(i)] = 1 << (i - ord('a'))

        # Initialize a list to keep track of the frequency of each character in the word
        countdict = [0] * 1024
        x = 0
        for i in word:
            x ^= tmp[i]
            countdict[x] += 1

        # Initialize the return value
        ret = 0

        # Calculate the number of wonderful substrings
        for k in range(1, 1024):
            v = countdict[k]
            if v == 0:
                continue
            if (k & (k - 1)) == 0:
                ret += v + int(v * (v - 1) / 2) + countdict[0] * v
                continue
            for i in tmp.values():
                if (k & i) == i:
                    ret += countdict[k - i] * v
            ret += int(v * (v - 1) / 2)

        # Add the number of wonderful substrings that contain only one character
        return ret + countdict[0] + int(countdict[0] * (countdict[0] - 1) / 2)
