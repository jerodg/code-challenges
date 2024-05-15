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

import "sort"

// maximumHappinessSum is a function that calculates the maximum sum of happiness that can be achieved
// by selecting k elements from a list of happiness values. The happiness values are sorted in ascending
// order and the function selects the k largest values. If a happiness value is negative, it is not
// included in the sum. The function returns the maximum sum as an int64.
//
// Parameters:
// happiness: A slice of integers representing the happiness values.
// k: An integer representing the number of elements to select.
//
// Returns:
// The maximum sum of happiness that can be achieved.
func maximumHappinessSum(happiness []int, k int) int64 {
	// The function sorts the happiness values in ascending order.
	sort.Ints(happiness)
	// res is the variable that keeps track of the maximum sum.
	res := 0
	// hLen is the number of happiness values.
	hLen := len(happiness) - 1
	// The function iterates over the k largest happiness values.
	for i := 0; i < k; i++ {
		// val is the current happiness value minus i.
		val := happiness[hLen-i] - i
		// If val is positive, the function adds it to res.
		if val > 0 {
			res += val
		}
	}
	// The function returns res as an int64.
	return int64(res)
}
