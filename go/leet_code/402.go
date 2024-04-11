package leet_code

// removeKdigits function takes a string representation of a number and an integer k,
// and returns the smallest possible number after removing k digits from the input number.
func removeKdigits(num string, k int) string {
	// Initialize an empty rune slice to store the result.
	result := []rune{}

	// Iterate over each character in the input number.
	for _, c := range num {
		// While the last digit in the result is greater than the current digit
		// and there are still digits to remove, remove the last digit from the result.
		for len(result) > 0 && result[len(result)-1] > c && k > 0 {
			result = result[:len(result)-1]
			k--
		}

		// If the result is not empty or the current digit is not '0', append the current digit to the result.
		if len(result) > 0 || c != '0' {
			result = append(result, c)
		}
	}

	// If there are still digits to remove after iterating over the input number,
	// remove the remaining digits from the end of the result.
	for len(result) > 0 && k > 0 {
		result = result[:len(result)-1]
		k--
	}

	// If the result is empty after removing digits, return "0".
	if len(result) <= 0 {
		return "0"
	}

	// Convert the result to a string and return it.
	return string(result)
}
