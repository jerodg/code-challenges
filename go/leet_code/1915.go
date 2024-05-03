// Package leet_code provides solutions for LeetCode problems.
package leet_code

// wonderfulSubstrings calculates the number of substrings in the given 'word' that contain at most
// one odd count of each letter.
//
// It uses a bitmask to keep track of the count of each letter in the substring. For each letter in
// the 'word', it toggles the corresponding bit in the mask.
// It then increments the frequency of the current mask and calculates the number of substrings that
// contain at most one odd count of each letter.
//
// Parameters:
// word: A string. It is expected to be non-empty and only contain lowercase letters.
//
// Returns:
// The number of substrings in 'word' that contain at most one odd count of each letter. The return
// type is int64.
// Time Complexity:
// Best-case: O(n), where n is the length of the input string 'word'.This is because the function
// iterates over the string once to calculate the frequency of each letter (mask).
// Worst-case: O(n), the function still iterates over the string once, regardless of the input.
// Average-case: O(n), the function's time complexity is linear in all cases.
// Space Complexity:
// The space complexity is O(1).This is because the function uses a constant amount of space to
// store the frequency of each letter (in an array of 1024 elements), regardless of the size of the
// input string.The variables res, mask, and mask2 also use a constant amount of space.Therefore,
// the space complexity is constant.
func wonderfulSubstrings(word string) int64 {
	// Initialize the result and the mask.
	res, mask := 0, 0

	// Initialize the frequency array.
	freq := make([]int, 1024)
	freq[0] = 1

	// For each letter in the word, toggle the corresponding bit in the mask and increment the frequency of the current mask.
	for i := 0; i < len(word); i++ {
		mask ^= 1 << (word[i] - 'a')
		freq[mask]++
	}

	// Calculate the number of substrings that contain at most one odd count of each letter.
	for mask := 0; mask < 1024; mask++ {
		if freq[mask] == 0 {
			continue
		}

		res += freq[mask] * (freq[mask] - 1) / 2
		for i := 0; i < 10; i++ {
			mask2 := mask ^ (1 << i)
			if mask2 < mask {
				res += freq[mask] * freq[mask2]
			}
		}
	}
	// Return the result.
	return int64(res)
}
