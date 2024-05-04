// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for removing duplicates from a sorted array in-place such that each element appears only once.
package leet_code

// removeDuplicates removes duplicates from a sorted array in-place such that each element appears only once.
//
// It accepts one parameter:
// - nums: a slice of integers representing the sorted array from which duplicates should be removed.
//
// The function returns an integer representing the new length of the array after duplicates have been removed.
//
// The function iterates over the array, replacing the first duplicate element with the current one if the current element is not equal to the previous one.
//
// Error Handling:
// - If the input array is empty, the function returns 0.
//
// Time complexity analysis:
// - Best-case: O(n), when the array has no duplicates.
// - Worst-case: O(n), when all elements in the array are duplicates.
// - Average-case: O(n), as we always have to iterate over each element of the array.
func removeDuplicates(nums []int) int {
	// If the array is empty, return 0
	if len(nums) == 0 {
		return 0
	}

	// i is the index of the first duplicate element
	i := 0

	// Iterate over the array starting from the second element
	for j := 1; j < len(nums); j++ {
		// If the current element is not equal to the previous one
		if nums[i] != nums[j] {
			// Increment the index of the first duplicate element
			i++

			// Replace the first duplicate element with the current one
			nums[i] = nums[j]
		}
	}

	// Return the new length of the array
	return i + 1
}
