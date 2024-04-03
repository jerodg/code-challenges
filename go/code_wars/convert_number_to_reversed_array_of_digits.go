package kata

import "strconv"

func Digitize(n int) []int {
	// Convert the integer to a string
	numStr := strconv.Itoa(n)

	// Create a slice to store the digits
	digits := make([]int, len(numStr))

	// Iterate over the string in reverse order
	for i := len(numStr) - 1; i >= 0; i-- {
		// Convert each character to an integer and store it in the slice
		digits[len(numStr)-i-1] = int(numStr[i] - '0')
	}

	return digits
}
