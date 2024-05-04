// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of removing the minimum number of parentheses to make a string valid.
// A string is valid if it is empty, or if it can be built by appending "(", ")", and valid strings.
// A string is balanced if it has as many "(" as ")".
package leet_code

// minRemoveToMakeValid removes the minimum number of parentheses to make a string valid.
//
// It accepts one parameter:
// - s: a string that only contains the characters '(', ')', and alphanumeric characters.
//
// The function returns a string that is a valid parentheses string and is a subsequence of s.
//
// The function uses a stack to keep track of the indices of the '(' characters.
// It iterates over the string, and for each character, if it is '(' it pushes its index to the stack, if it is ')' and the stack is empty, it adds its index to the remove slice, otherwise, it pops an index from the stack.
// After the iteration, it adds the remaining indices in the stack to the remove slice.
// It then constructs the result string by skipping the characters at the indices in the remove slice.
//
// Time complexity analysis:
// - Best-case: O(n), when the string is already valid.
// - Worst-case: O(n), when all characters are '(' or ')'.
// - Average-case: O(n), as we always have to iterate over each character in the string.
func minRemoveToMakeValid(s string) string {
	var stack []int
	var remove []int
	for i, v := range s {
		if v == '(' {
			stack = append(stack, i)
		} else if v == ')' {
			if len(stack) == 0 {
				remove = append(remove, i)
			} else {
				stack = stack[:len(stack)-1]
			}
		}
	}
	remove = append(remove, stack...)
	var res []byte
	for i, v := range s {
		if len(remove) > 0 && i == remove[0] {
			remove = remove[1:]
			continue
		}
		res = append(res, byte(v))
	}
	return string(res)
}
