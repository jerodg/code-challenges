// Package leet_code provides solutions for LeetCode problems.
package leet_code

import "math"

// minFallingPathSum calculates the minimum sum of a falling path through grid.
// A falling path starts at any element in the first row, and chooses one element from each row.
// The next row's choice must be in a column that is different from the previous row's column by at
// most one.
//
// Parameters:
// grid: A 2D integer array representing the grid. The grid has dimensions m x n where
// 1 <= m, n <= 100.
//
//	Each grid[i][j] will be a number in the range [1, 100].
//
// Returns:
// int: The minimum sum of a falling path through grid.
//
// Time Complexity:
// The time complexity of the function is O(mn), where m is the number of rows in
// the grid and n is the number of columns.This is because the function iterates over each cell in
// the grid exactly once.Therefore, the best-case, worst-case, and average time
// complexity are all O(mn).
// Space Complexity:
// The space complexity of the function is O(n), where n is the number of columns in the grid.
// This is because the function uses two arrays, vars and newVars, each of size n, to store the
// minimum sum of a falling path ending at each column in the current and next row,
// respectively. The space used by these arrays does not increase with the size of the grid, so the
// space complexity is linear.
func minFallingPathSum(grid [][]int) int {
	// vars is an array that stores the minimum sum of a falling path ending at each column in the
	// current row.
	vars := make([]int, 4)
	for row := len(grid) - 1; row >= 0; row-- {
		// newVars is an array that stores the minimum sum of a falling path ending at each column
		// in the next row.
		newVars := make([]int, 4)
		for i := 0; i < 4; i++ {
			newVars[i] = math.MaxInt32
		}
		for col := 0; col < len(grid[0]); col++ {
			// x is the sum of the current cell value and the minimum sum of a falling path ending
			// at the previous row.
			x := grid[row][col]
			if col != vars[0] {
				x += vars[1]
			} else {
				x += vars[3]
			}
			// Update newVars if the current sum is less than the stored minimum sum.
			if x <= newVars[1] {
				newVars[2] = newVars[0]
				newVars[3] = newVars[1]
				newVars[0] = col
				newVars[1] = x
			} else if x <= newVars[3] {
				newVars[2] = col
				newVars[3] = x
			}
		}
		// Update vars for the next iteration.
		vars = newVars
	}
	// Return the minimum sum of a falling path through grid.
	return min(vars[1], vars[3])
}
