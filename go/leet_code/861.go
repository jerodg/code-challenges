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

import "math"

// matrixScore is a function that calculates the maximum score that can be achieved by flipping
// the rows and columns of a binary matrix. The score of a matrix is defined as the sum of its
// elements, where each row of the matrix is interpreted as a binary number.
//
// Parameters:
// grid: A 2D slice of integers representing the binary matrix.
//
// Returns:
// The maximum score that can be achieved.
func matrixScore(grid [][]int) int {
	// r and c are the number of rows and columns in the grid, respectively.
	r, c := len(grid), len(grid[0])
	// answer is the initial score, assuming all rows start with 1 after flipping.
	answer := (1 << (c - 1)) * r
	for j := 1; j < c; j++ {
		// temp is the value of the current column as a binary number.
		temp := 1 << (c - 1 - j)
		// t is the number of 1s in the current column.
		t := 0
		for i := 0; i < r; i++ {
			// If the current cell is the same as the first cell in its row, increment t.
			if grid[i][j] == grid[i][0] {
				t++
			}
		}
		// Add the maximum of t and r-t to the answer, multiplied by temp.
		answer += int(math.Max(float64(t), float64(r-t))) * temp
	}
	return answer
}
