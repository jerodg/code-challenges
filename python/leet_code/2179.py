"""LeetCode 2179. Count Good Triplets in an Array.

Copyright ©2010-2025 JerodG <https://github.com/jerodg/>.
Licensed under the Server Side Public License (SSPL).
"""
from sortedcontainers import SortedList


class Solution:
    """Solution for LeetCode 2179: Count Good Triplets in an Array.

    Implements an efficient algorithm to count good triplets between two permutation arrays
    using a sorted list data structure for optimized lookups.
    """

    def goodTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        """Count good triplets between two arrays.

        A triplet (i,j,k) is good if the relative ordering of these elements
        is the same in both arrays where 0 ≤ i < j < k < len(nums1).

        Args:
            nums1: First array (permutation of 0 to n-1)
            nums2: Second array (permutation of 0 to n-1)

        Returns:
            Number of good triplets

        Algorithm:
            1. Map positions of elements in nums1
            2. Convert nums2 elements to their positions in nums1
            3. Process in reverse to count triplets using a sorted list

        Time complexity: O(n log n)
        Space complexity: O(n)
        """
        res, inds, arr = 0, [0] * len(nums1), SortedList()
        for i, num in enumerate(nums1):
            inds[num] = i
        for i, num in enumerate(nums2):
            nums1[i] = inds[num]
        for i, num in enumerate(nums1[::-1]):
            ind = arr.bisect(num)
            res += (i - ind) * (num - ind)
            arr.add(num)

        return res
