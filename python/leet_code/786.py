"""
leet_code/786.py

Copyright ©2012-2024 JerodG <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""


class Solution:
    """
    This class provides a solution for finding the Kth smallest prime fraction from a list of integers.
    """

    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        """
        This method finds the Kth smallest prime fraction from a list of integers.

        Parameters:
        arr (list[int]): A list of integers.
        k (int): The Kth smallest prime fraction to find.

        Returns:
        list[int]: The Kth smallest prime fraction as a list of two integers [numerator, denominator].
        """

        def con(value):
            """
            This helper function calculates the number of fractions that are less than the given value,
            and also finds the largest fraction that is less than the given value.

            Parameters:
            value (float): The value to compare the fractions with.

            Returns:
            tuple: A tuple containing the number of fractions that are less than the given value,
            and the numerator and denominator of the largest fraction that is less than the given value.
            """

            nb_smallest_fraction = 0
            numer = arr[0]
            denom = arr[-1]

            slow = 0
            for fast in range(1, len(arr)):
                while slow < fast and arr[slow] / arr[fast] < value:
                    if arr[slow] / arr[fast] > numer / denom:
                        numer, denom = arr[slow], arr[fast]

                    slow += 1

                nb_smallest_fraction += slow

            return nb_smallest_fraction, numer, denom

        l = arr[0] / arr[-1]
        r = 1

        # Binary search for the Kth smallest prime fraction
        while l < r:
            m = (l + r) / 2

            count, numer, denom = con(m)

            if count == k:
                return [numer, denom]

            if count > k:
                r = m
            else:
                l = m
