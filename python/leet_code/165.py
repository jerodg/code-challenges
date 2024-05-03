"""leet_code/165.py

This module contains a solution for comparing two version numbers (version1 and version2).
The version numbers are in the format of 'x.y.z....' where x, y, z are non-negative integers.
The comparison is done by comparing each corresponding pair of integer values in the version numbers.

Classes:
    Solution: This class contains a method to compare two version numbers.
"""


class Solution:
    """A class used to compare two version numbers.

    Methods:
        compareVersion: Compares two version numbers and returns an integer indicating the result.
    """

    def compareVersion(self, version1: str, version2: str) -> int:
        """Compares two version numbers.

        Args:
            version1 (str): The first version number in the format 'x.y.z....'.
            version2 (str): The second version number in the format 'x.y.z....'.

        Returns:
            int: Returns 1 if version1 is greater than version2, -1 if version1 is less than version2,
                 and 0 if both versions are equal.

        This function does not handle errors explicitly. If the input is not in the expected format,
        Python's built-in error handling will raise an exception. For example, if the version numbers
        do not contain integers or if they are not separated by '.', a ValueError will be raised.
        """
        # Split the version numbers by '.'
        version1 = version1.split('.')
        version2 = version2.split('.')

        # Get the minimum length of the two version numbers
        ml = min(len(version1), len(version2))

        # Compare each corresponding pair of integers in the version numbers
        for i in range(ml):
            v1 = int(version1[i])
            v2 = int(version2[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        # If the version numbers have different lengths, check the remaining integers in the longer version number
        version = version1 if len(version1) - ml > 0 else version2
        v = 1 if len(version1) - ml > 0 else 2
        for i in range(ml, len(version)):
            if int(version[i]) > 0:
                return 1 if v == 1 else -1

        # If all corresponding pairs of integers are equal, the version numbers are equal
        return 0
