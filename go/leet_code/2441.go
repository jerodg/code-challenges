// Package leet_code provides solutions for LeetCode problems.
package leet_code

import "slices"

// findMaxK finds the maximum integer 'k' in the given slice 'nums' such that both 'k' and '-k' exist in 'nums'.
// If no such integer exists, it returns -1.
//
// It first sorts the slice and then checks for each number from the end if its negative counterpart exists in the slice.
//
// Parameters:
// nums: A slice of integers. It is expected to be non-empty.
//
// Returns:
// The maximum integer 'k' such that both 'k' and '-k' exist in 'nums'. If no such integer exists, it returns -1.
func findMaxK(nums []int) int {
	// Sort the slice in ascending order.
	slices.Sort(nums)

	// Create a map to store the existence of each number in the slice.
	m := make(map[int]bool, len(nums))

	// Populate the map with the numbers in the slice.
	for _, num := range nums {
		m[num] = true
	}

	// Check for each number from the end if its negative counterpart exists in the slice.
	for i := len(nums) - 1; i > 0; i-- {
		if m[-nums[i]] {
			// If the negative counterpart exists, return the number.
			return nums[i]
		}
	}
	// If no such number exists, return -1.
	return -1
}
