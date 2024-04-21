// Package leet_code provides solutions for LeetCode problems.
package leet_code

// removeDuplicates removes duplicates from a sorted array in-place such that each element appears only once.
// It returns the new length of the array.
//
// Parameters:
//  - nums: A sorted integer array from which duplicates should be removed.
//
// Returns:
//  - The new length of the array after duplicates have been removed.
//
// Error Handling:
//  - If the input array is empty, the function returns 0.
//
// Example Usage:
//  nums := []int{1, 1, 2}
//  length := removeDuplicates(nums) // length: 2, nums: [1, 2]
func removeDuplicates(nums []int) int {
	// If the array is empty, return 0
	if len(nums) == 0 {
		return 0
	}

	// Initialize the index of the first duplicate element
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
