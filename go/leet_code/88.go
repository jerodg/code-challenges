// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of merging two sorted arrays.
package leet_code

// merge merges two sorted arrays in-place.
//
// It accepts four parameters:
// - nums1: a slice of integers representing the first sorted array.
// - m: an integer representing the number of initialized elements in nums1.
// - nums2: a slice of integers representing the second sorted array.
// - n: an integer representing the number of initialized elements in nums2.
//
// The function does not return a value. It modifies nums1 in-place to include the elements of nums2 in sorted order.
//
// The function iterates from the end of nums1, comparing the last elements of nums1 and nums2, and placing the larger one at the current position.
// If all elements in nums1 are processed (m == 0), the remaining elements in nums2 are copied to nums1.
// If all elements in nums2 are processed (n == 0), the function returns as the remaining elements in nums1 are already in place.
//
// Time complexity analysis:
// - Best-case: O(n), when all elements in nums1 are larger than those in nums2.
// - Worst-case: O(n), when all elements in nums2 are larger than those in nums1.
// - Average-case: O(n), as we always have to iterate over each element in nums1 and nums2.
func merge(nums1 []int, m int, nums2 []int, n int) {
	for i := m + n - 1; i >= 0; i-- {
		if m == 0 {
			nums1[i] = nums2[n-1]
			n--
			continue
		}

		if n == 0 {
			return
		}

		if nums1[m-1] > nums2[n-1] {
			nums1[i] = nums1[m-1]
			m--
		} else {
			nums1[i] = nums2[n-1]
			n--
		}
	}
}
