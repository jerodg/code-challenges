// Copyright © 2010-2024 JerodG <https://github.com/jerodg/>
//
// This program is free software: you can redistribute it and/or modify it under the terms of the
// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
// or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
// for more details.
//
// The above copyright notice and this permission notice shall be included in all copies or
// substantial portions of the Software. You should have received a copy of the SSPL along with this
// program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

// Package leet_code contains solutions for problems from LeetCode.
package leet_code

// kthSmallestPrimeFraction is a function that calculates the k-th smallest prime fraction from a sorted list of prime numbers.
// A fraction is defined as a number of the form a/b where a and b are both integers and b != 0. A prime fraction is a fraction
// where both a and b are prime numbers. The function uses a binary search algorithm to find the k-th smallest prime fraction.
//
// Parameters:
// arr: A slice of integers representing the sorted list of prime numbers.
// k: An integer representing the k-th smallest prime fraction to find.
//
// Returns:
// A slice of two integers representing the k-th smallest prime fraction. The first integer is the numerator and the second integer is the denominator.
func kthSmallestPrimeFraction(arr []int, k int) []int {
	// lo and hi are the lower and upper bounds of the binary search, respectively.
	lo, hi := 0.0, 1.0
	// n is the number of prime numbers in the list.
	n := len(arr)
	// The function performs a binary search until lo is no longer less than hi.
	for lo < hi {
		// mid is the midpoint of lo and hi.
		mid := (lo + hi) / 2
		// j is the index of the current prime number in the list.
		j := 1
		// samllerOrEqual is the number of fractions that are smaller or equal to mid.
		samllerOrEqual := 0
		// curMax is the maximum fraction found so far that is smaller or equal to mid.
		curMax := 0.0
		// resI and resJ are the indices of the prime numbers that form the maximum fraction found so far.
		resI, resJ := 0, 0
		// The function iterates over each prime number in the list.
		for i := 0; i < n; i++ {
			// The function finds the first prime number that forms a fraction with the current prime number that is smaller than mid.
			for j < n && float64(arr[i])/float64(arr[j]) >= mid {
				j++
			}
			// The function increments samllerOrEqual by the number of fractions that are smaller or equal to mid.
			samllerOrEqual += n - j
			// If the current fraction is smaller or equal to mid and larger than curMax, the function updates curMax and resI and resJ.
			if j < n && curMax < float64(arr[i])/float64(arr[j]) {
				curMax = float64(arr[i]) / float64(arr[j])
				resI, resJ = i, j
			}
		}
		// If samllerOrEqual is equal to k, the function returns the k-th smallest prime fraction.
		if samllerOrEqual == k {
			return []int{arr[resI], arr[resJ]}
		}
		// If samllerOrEqual is larger than k, the function updates hi to mid.
		if samllerOrEqual > k {
			hi = mid
		} else {
			// If samllerOrEqual is smaller than k, the function updates lo to mid and adds a small number to avoid infinite loops.
			lo = mid + 0.0000000001
		}
	}
	// If the function cannot find the k-th smallest prime fraction, it returns nil.
	return nil
}
