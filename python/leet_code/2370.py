"""
leet_code/2370.py

This module contains a solution for finding the longest ideal string given a string and an integer.
The solution is encapsulated within the Solution class.

The Solution class has a single static method, longestIdealString, which calculates the longest ideal string.
An ideal string is defined as a string where the ASCII value of each character is within a range of k from the previous character.

This module is compatible with Python 3.12 and follows PEP and Google Style Guide standards.
"""


class Solution:
    @staticmethod
    def longestIdealString(s: str, k: int) -> int:
        """
        Calculate the longest ideal string from the given string and integer.

        An ideal string is defined as a string where the ASCII value of each character is within a range of k from the previous character.

        Args:
            s (str): The input string to be processed. It is expected to be a string of ASCII characters.
            k (int): The range within which the ASCII value of each character in the string should be from the previous character.

        Returns:
            int: The length of the longest ideal string that can be formed from the input string.

        This function does not handle errors as it expects the inputs to be of the correct type and within the valid range.
        """
        # Initialize a list to store the maximum length of ideal string ending with each ASCII character
        l = [0] * 128
        for c in s:
            # Get the ASCII value of the character
            i = ord(c)
            # Update the maximum length of ideal string ending with the current character
            l[i] = max(l[i - k: i + k + 1]) + 1
        # Return the maximum length among all characters
        return max(l)
