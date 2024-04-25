// Package leet_code provides solutions for LeetCode problems.
package leet_code

// maximum is a function that takes two integers as parameters and returns the larger of the two.
//
// Parameters:
// a: The first integer to compare.
// b: The second integer to compare.
//
// Returns:
// The larger of the two input integers.
func maximum(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// minimum is a function that takes two integers as parameters and returns the smaller of the two.
//
// Parameters:
// a: The first integer to compare.
// b: The second integer to compare.
//
// Returns:
// The smaller of the two input integers.
func minimum(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// longestIdealString is a function that takes a string and an integer as parameters and returns the length of the longest ideal string.
// An ideal string is defined as a string where the difference between the ASCII values of any two characters is less than or equal to k.
//
// Parameters:
// s: The input string.
// k: The maximum allowed difference between the ASCII values of any two characters in an ideal string.
//
// Returns:
// The length of the longest ideal string that can be formed from the input string.
//
// Error Handling:
// If the input string is empty, the function returns 0.
func longestIdealString(s string, k int) int {
	dp := make([]int, 27)
	n := len(s)

	for i := n - 1; i >= 0; i-- {
		cc := s[i]
		idx := int(cc - 'a')
		maxi := -1 << 31

		left := maximum(idx-k, 0)
		right := minimum(idx+k, 26)

		for j := left; j <= right; j++ {
			maxi = maximum(maxi, dp[j])
		}

		dp[idx] = maxi + 1
	}

	maximum := -1 << 31
	for _, val := range dp {
		if val > maximum {
			maximum = val
		}
	}

	return maximum
}
