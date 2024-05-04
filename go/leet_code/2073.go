// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of calculating the time required to buy a ticket.
// The time required to buy a ticket is the sum of the number of tickets each person in front of you has, including yourself.
// If a person has more tickets than you, you only count the number of tickets you have.
// If a person has fewer tickets than you or the same number of tickets and is not standing in front of you, you count the number of tickets they have.
package leet_code

// timeRequiredToBuy calculates the time required to buy a ticket.
//
// It accepts two parameters:
// - tickets: a slice of integers where each integer represents the number of tickets a person has.
// - k: an integer representing your position in the queue (0-indexed).
//
// The function returns an integer representing the time required to buy a ticket.
//
// The function iterates over the queue, and for each person, it adds the minimum number of tickets between the person and you to the result.
//
// Time complexity analysis:
// - Best-case: O(n), when you are at the front of the queue.
// - Worst-case: O(n), when you are at the back of the queue.
// - Average-case: O(n), as we always have to iterate over each person in the queue.
//
// Space complexity: O(1), as we only use a constant amount of space to store the result and the number of your tickets.
func timeRequiredToBuy(tickets []int, k int) int {
	result := 0
	c := tickets[k]
	for i, n := range tickets {
		if i == k {
			result += c
		} else if i < k {
			result += minimum(c, n)
		} else {
			result += minimum(c-1, n)
		}
	}
	return result
}

// minimum returns the minimum of two integers.
//
// It accepts two parameters:
// - a, b: the two integers to compare.
//
// The function returns an integer representing the minimum of a and b.
//
// Time complexity: O(1), as we only perform a constant amount of operations.
// Space complexity: O(1), as we only use a constant amount of space to store the result.
func minimum(a, b int) int {
	if a < b {
		return a
	}
	return b
}
