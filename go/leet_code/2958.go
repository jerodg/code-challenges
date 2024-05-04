// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of finding the maximum length of a subarray with at most 'k' distinct elements.
package leet_code

// maxSubarrayLength finds the maximum length of a subarray with at most 'k' distinct elements.
//
// It accepts two parameters:
// - nums: a slice of integers representing the array.
// - k: an integer representing the maximum number of distinct elements in a subarray.
//
// The function returns an integer representing the maximum length of a subarray with at most 'k' distinct elements.
//
// The function uses a sliding window approach with two pointers, 'left' and 'right', and a counter map to keep track of the number of each element in the current subarray.
// It iterates over the array, and for each element, it increments its count in the counter map.
// If the count of the current element is more than 'k', it moves the 'left' pointer to the right until the count of the current element is not more than 'k'.
// After each iteration, it updates the maximum length if the length of the current subarray is greater than the maximum length.
//
// Time complexity analysis:
// - Best-case: O(n), when 'k' is equal to the number of distinct elements in the array.
// - Worst-case: O(n), when 'k' is less than the number of distinct elements in the array.
// - Average-case: O(n), as we always have to iterate over each element in the array.
//
// Space complexity: O(n), as we use a map to store the count of each element in the array.
func maxSubarrayLength(nums []int, k int) int {
	left := 0
	counter := make(map[int]int)
	maxLength := 0
	for right, num := range nums {
		counter[num]++
		for counter[num] > k {
			counter[nums[left]]--
			if counter[nums[left]] == 0 {
				delete(counter, nums[left])
			}
			left++
		}
		if right-left+1 > maxLength {
			maxLength = right - left + 1
		}
	}
	return maxLength
}
