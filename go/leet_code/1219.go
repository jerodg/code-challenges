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

// getMaximumGold is a function that calculates the maximum amount of gold that can be collected
// from a grid. The grid is a 2D slice of integers where each integer represents the amount of gold
// at that location. The function traverses the grid, starting from each cell that contains gold,
// and collects gold along the way. The traversal stops when it hits a cell with no gold or a cell
// that has been visited before. The function returns the maximum amount of gold that can be collected.
//
// Parameters:
// grid: A 2D slice of integers representing the grid.
//
// Returns:
// The maximum amount of gold that can be collected.
func getMaximumGold(grid [][]int) int {
	// sol is the variable that keeps track of the maximum amount of gold collected so far.
	sol := 0
	for i := range grid {
		for j := range grid[i] {
			// Only start traversal if the current cell contains gold.
			if grid[i][j] != 0 {
				// seen is a 2D slice that keeps track of the cells that have been visited.
				seen := make([][]bool, len(grid))
				for i := range seen {
					seen[i] = make([]bool, len(grid[i]))
				}
				seen[i][j] = true
				// curr is the amount of gold collected in the current traversal.
				curr := traverse(i, j, grid, seen)
				// Update sol if the current traversal collected more gold.
				if sol < curr {
					sol = curr
				}
			}
		}
	}
	return sol
}

// traverse is a helper function that performs a depth-first search (DFS) on the grid from a given
// starting cell. It collects gold along the way and returns the total amount of gold collected.
//
// Parameters:
// i, j: The coordinates of the starting cell.
// grid: The grid.
// seen: A 2D slice that keeps track of the cells that have been visited.
//
// Returns:
// The total amount of gold collected in the traversal.
func traverse(i, j int, grid [][]int, seen [][]bool) int {
	// sol is the variable that keeps track of the total amount of gold collected in the traversal.
	sol := grid[i][j]
	// The following four if blocks check the four possible directions (up, down, left, right) that
	// the traversal can go to from the current cell. If a direction is valid (i.e., within the grid,
	// not visited before, and contains gold), the function recursively calls itself in that direction.
	if i-1 >= 0 && !seen[i-1][j] && grid[i-1][j] > 0 {
		seen[i-1][j] = true
		temp := traverse(i-1, j, grid, seen)
		if sol < temp+grid[i][j] {
			sol = temp + grid[i][j]
		}
		seen[i-1][j] = false
	}
	if i+1 < len(grid) && !seen[i+1][j] && grid[i+1][j] > 0 {
		seen[i+1][j] = true
		temp := traverse(i+1, j, grid, seen)
		if sol < temp+grid[i][j] {
			sol = temp + grid[i][j]
		}
		seen[i+1][j] = false
	}
	if j-1 >= 0 && !seen[i][j-1] && grid[i][j-1] > 0 {
		seen[i][j-1] = true
		temp := traverse(i, j-1, grid, seen)
		if sol < temp+grid[i][j] {
			sol = temp + grid[i][j]
		}
		seen[i][j-1] = false
	}
	if j+1 < len(grid[i]) && !seen[i][j+1] && grid[i][j+1] > 0 {
		seen[i][j+1] = true
		temp := traverse(i, j+1, grid, seen)
		if sol < temp+grid[i][j] {
			sol = temp + grid[i][j]
		}
		seen[i][j+1] = false
	}
	return sol
}
