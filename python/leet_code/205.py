"""
This module provides a solution for determining if two strings are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t, with preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

This module requires Python 3.12 and uses a dictionary for mapping the characters.

Example Usage:
    >>> s = Solution()
    >>> s.isIsomorphic('egg', 'add')
    True
    >>> s.isIsomorphic('foo', 'bar')
    False
    >>> s.isIsomorphic('paper', 'title')
    True
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Determines if two strings are isomorphic.

        This function creates a dictionary to store the mapping of characters from string s to string t.
        It then iterates over the characters in the strings. If a character in s is already mapped,
        it checks if the mapping is correct. If a character in s is not mapped, it checks if the character in t is already mapped.

        Args:
            s (str): The first string to compare.
            t (str): The second string to compare.

        Returns:
            bool: True if the strings are isomorphic, False otherwise.

        Raises:
            ValueError: If the lengths of the strings are not equal.

        Doctest:
            >>> s = Solution()
            >>> s.isIsomorphic('egg', 'add')
            True
            >>> s.isIsomorphic('foo', 'bar')
            False
            >>> s.isIsomorphic('paper', 'title')
            True
        """
        # Check if the lengths of the strings are equal
        if len(s) != len(t):
            raise ValueError('The lengths of the strings must be equal.')

        # Create a dictionary to store the mapping of characters
        mapping = {}

        # Iterate over the characters in the strings
        for i in range(len(s)):
            # Check if the character in s is already mapped
            if s[i] in mapping:
                # Check if the mapping is correct
                if mapping[s[i]] != t[i]:
                    return False
            else:
                # Check if the character in t is already mapped
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]

        return True
