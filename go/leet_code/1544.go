// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of making a string good.
// A string is good if it does not have two adjacent characters that are the same, but one is uppercase and the other is lowercase.
package leet_code

// makeGood makes a string good.
//
// It accepts one parameter:
// - s: a string that only contains lowercase and uppercase English letters.
//
// The function returns a string that is a good string and is a subsequence of s.
//
// The function uses a stack to keep track of the characters in the string.
// It iterates over the string, and for each character, if the stack is not empty and the top character of the stack is the same as the current character but with different case, it pops the top character from the stack, otherwise, it pushes the current character to the stack.
//
// Time complexity analysis:
// - Best-case: O(n), when the string is already good.
// - Worst-case: O(n), when all characters are the same but with alternating cases.
// - Average-case: O(n), as we always have to iterate over each character in the string.
func makeGood(s string) string {
	stack := make([]byte, 0)
	for i := 0; i < len(s); i++ {
		if len(stack) == 0 {
			stack = append(stack, s[i])
			continue
		}
		if stack[len(stack)-1] == s[i]+32 || stack[len(stack)-1] == s[i]-32 {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, s[i])
		}
	}
	return string(stack)
}
