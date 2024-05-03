// Package leet_code provides solutions for LeetCode problems.
package leet_code

import (
	"strconv"
	"strings"
)

// compareVersion compares two version strings and returns an integer according to the comparison result.
// It splits the version strings by ".", converts each part to an integer, and compares them part by part.
// If version1 is greater than version2, it returns 1.
// If version1 is less than version2, it returns -1.
// If version1 is equal to version2, it returns 0.
//
// Parameters:
// version1: A string representing the first version to compare. It should be a non-empty string consisting of digits and periods.
// version2: A string representing the second version to compare. It should be a non-empty string consisting of digits and periods.
//
// Returns:
// An integer indicating the comparison result. It returns 1 if version1 > version2, -1 if version1 < version2, and 0 if version1 = version2.
func compareVersion(version1 string, version2 string) int {
	// Split the version strings by "."
	rev1 := strings.Split(version1, ".")
	rev2 := strings.Split(version2, ".")

	// Convert each part of the version strings to an integer
	revInt1 := make([]int, len(rev1))
	revInt2 := make([]int, len(rev2))

	for i := 0; i < len(rev1); i++ {
		revInt1[i], _ = strconv.Atoi(rev1[i])
	}
	for i := 0; i < len(rev2); i++ {
		revInt2[i], _ = strconv.Atoi(rev2[i])
	}

	// Compare the integer parts of the version strings
	i := 0
	j := 0

	for i < len(revInt1) && j < len(revInt2) {
		if revInt1[i] < revInt2[j] {
			return -1
		} else if revInt1[i] > revInt2[j] {
			return 1
		}
		i++
		j++
	}

	// Check the remaining parts of the version strings
	for i < len(revInt1) {
		if revInt1[i] > 0 {
			return 1
		}
		i++
	}
	for j < len(revInt2) {
		if revInt2[j] > 0 {
			return -1
		}
		j++
	}

	// If all parts are equal, return 0
	return 0
}
