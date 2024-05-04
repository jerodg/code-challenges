// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of checking if a string is valid.
// The string is valid if it can be made valid by inserting parentheses at any position.
// The function assumes that the string only contains the characters '(', ')', and '*'.
package leet_code

// checkValidString checks if a string is valid.
//
// It accepts one parameter:
// - s: a string that only contains the characters '(', ')', and '*'.
//
// The function returns a boolean indicating whether the string is valid.
//
// The function uses two counters to simulate the possible range of the number of open parentheses.
// It iterates over the string, updating the counters.
// If at any point during the iteration the right counter is less than zero, the function returns false.
// After the iteration, the function returns whether the left counter is zero.
//
// Time complexity analysis:
// - Best-case: O(n), when the string is valid.
// - Worst-case: O(n), when the string is not valid.
// - Average-case: O(n), as we always have to iterate over each character in the string.
func checkValidString(s string) bool {
	left, right := 0, 0
	for _, c := range s {
		if c == '(' {
			left++
		} else {
			left--
		}
		if c != ')' {
			right++
		} else {
			right--
		}
		if right < 0 {
			break
		}
		left = max(left, 0)
	}
	return left == 0
}

// max returns the maximum of two integers.
//
// It accepts two parameters:
// - a, b: the two integers to compare.
//
// The function returns the maximum of a and b.
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
