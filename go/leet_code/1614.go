// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of finding the maximum depth of valid parentheses in a string.
// The depth of the parentheses in a string is the maximum number of levels of nested parentheses.
// A string is valid if it is empty, or if it can be built by appending "(", ")", and valid strings.
package leet_code

// maxDepth finds the maximum depth of valid parentheses in a string.
//
// It accepts one parameter:
// - s: a string that only contains the characters '(', ')', and alphanumeric characters.
//
// The function returns an integer representing the maximum depth of valid parentheses in the string.
//
// The function uses a counter to keep track of the current depth of parentheses and a variable to keep track of the maximum depth.
// It iterates over the string, and for each character, if it is '(' it increments the counter, if it is ')' it decrements the counter.
// After each increment, it updates the maximum depth if the current depth is greater than the maximum depth.
//
// Time complexity analysis:
// - Best-case: O(n), when the string is already valid.
// - Worst-case: O(n), when all characters are '(' or ')'.
// - Average-case: O(n), as we always have to iterate over each character in the string.
func maxDepth(s string) int {
	var max, count int
	for _, c := range s {
		if c == '(' {
			count++
			if count > max {
				max = count
			}
		} else if c == ')' {
			count--
		}
	}
	return max
}
