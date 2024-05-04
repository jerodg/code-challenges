// Package kata provides solutions to problems from CodeWars.
//
// This particular file provides a solution to the problem of converting a number to a reversed array of digits.
package kata

import "strconv"

// Digitize converts a number to a reversed array of digits.
//
// It accepts one parameter:
// - n: an integer that needs to be converted to a reversed array of digits.
//
// The function returns a slice of integers representing the digits of the input number in reverse order.
//
// The function converts the input number to a string, then iterates over the string in reverse order,
// converting each character back to an integer and storing it in a slice.
//
// Time complexity analysis:
// - Best-case: O(n), when the number has only one digit.
// - Worst-case: O(n), when the number has multiple digits.
// - Average-case: O(n), as we always have to iterate over each digit of the number.
func Digitize(n int) []int {
	// numStr is the string representation of the input number.
	numStr := strconv.Itoa(n)

	// digits is a slice to store the digits of the input number in reverse order.
	digits := make([]int, len(numStr))

	// Iterate over the string in reverse order.
	for i := len(numStr) - 1; i >= 0; i-- {
		// Convert each character to an integer and store it in the slice.
		digits[len(numStr)-i-1] = int(numStr[i] - '0')
	}

	// Return the slice of digits in reverse order.
	return digits
}
