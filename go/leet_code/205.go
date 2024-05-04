// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of determining if two strings are isomorphic.
// Two strings s and t are isomorphic if the characters in s can be replaced to get t.
// All occurrences of a character must be replaced with another character while preserving the order of characters.
// No two characters may map to the same character, but a character may map to itself.
package leet_code

// isIsomorphic determines if two strings are isomorphic.
//
// It accepts two parameters:
// - s: a string representing the first string.
// - t: a string representing the second string.
//
// The function returns a boolean indicating whether the two strings are isomorphic.
//
// The function creates two maps to track the mapping from s to t and from t to s.
// It iterates over the strings, checking and updating the mappings.
// If a mapping that violates the isomorphism is found, the function returns false.
//
// Error Handling:
// - If the lengths of s and t are not equal, the function returns false.
//
// Time complexity analysis:
// - Best-case: O(n), when the strings are isomorphic.
// - Worst-case: O(n), when the strings are not isomorphic.
// - Average-case: O(n), as we always have to iterate over each character in the strings.
func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	m1 := make(map[byte]byte)
	m2 := make(map[byte]byte)

	for i := 0; i < len(s); i++ {
		if _, ok := m1[s[i]]; !ok {
			m1[s[i]] = t[i]
		} else if m1[s[i]] != t[i] {
			return false
		}

		if _, ok := m2[t[i]]; !ok {
			m2[t[i]] = s[i]
		} else if m2[t[i]] != s[i] {
			return false
		}
	}

	return true
}
