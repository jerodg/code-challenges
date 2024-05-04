// Package leet_code provides solutions to problems from LeetCode.
//
// This particular file provides a solution to the problem of determining the minimum number of rescue
// boats needed to save people of different weights, given a weight limit for each boat.
package leet_code

// numRescueBoats calculates the minimum number of boats required to rescue all people.
//
// It accepts two parameters:
// - people: a slice of integers representing the weights of the people to be rescued.
// - limit: an integer representing the maximum weight that a single boat can carry.
//
// The function returns an integer representing the minimum number of boats required.
//
// The function uses a greedy algorithm to pair the heaviest and lightest person until this is no longer
// possible. Then it rescues the heaviest person left. This process is repeated until all people are rescued.
//
// Time complexity analysis:
// - Best-case: O(n), when all people have the same weight.
// - Worst-case: O(n), when all people have different weights.
// - Average-case: O(n), as we always have to check each person's weight.
func numRescueBoats(people []int, limit int) int {
	// weightCount is a frequency map where the index is the weight and the value is the count of
	// people with that weight.
	weightCount := make([]int, limit+1)
	for _, weight := range people {
		weightCount[weight]++
	}

	// left and right are pointers to the lightest and heaviest person not yet rescued.
	left, right := 1, limit
	// boats is the count of boats used.
	boats := 0

	// Loop until all people are rescued.
	for left <= right {
		// Find the next lightest person not yet rescued.
		for left <= right && weightCount[left] == 0 {
			left++
		}
		// Find the next heaviest person not yet rescued.
		for left <= right && weightCount[right] == 0 {
			right--
		}

		// If all people are rescued, break the loop.
		if left > right {
			break
		}

		// Rescue the heaviest person.
		weightCount[right]--
		boats++

		// If possible, also rescue the lightest person.
		if left+right <= limit && weightCount[left] > 0 {
			weightCount[left]--
		}
	}
	// Return the number of boats used.
	return boats
}
