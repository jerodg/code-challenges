// Package leet_code provides solutions for LeetCode problems.
package leet_code

// removeElement removes all instances of a specific value in-place from an integer array.
// It returns the new length of the array.
//
// Parameters:
//  - nums: An integer array from which the specified value should be removed.
//  - val: The value to be removed from the array.
//
// Returns:
//  - The new length of the array after the specified value has been removed.
//
// Error Handling:
//  - If the input array is empty, the function returns 0.
//
// Example Usage:
//  nums := []int{3, 2, 2, 3}
//  val := 3
//  length := removeElement(nums, val) // length: 2, nums: [2, 2]
func removeElement(nums []int, val int) int {
	// Initialize the index of the first occurrence of the specified value
	var i int

	// Iterate over the array
	for j := 0; j < len(nums); j++ {
		// If the current element is not equal to the specified value
		if nums[j] != val {
			// Replace the first occurrence of the specified value with the current element
			nums[i] = nums[j]

			// Increment the index of the first occurrence of the specified value
			i++
		}
	}

	// Return the new length of the array
	return i
}
