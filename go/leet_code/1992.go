// Package leet_code provides solutions for LeetCode problems.
package leet_code

// findFarmland identifies all farmland plots in a given 2D grid.
// A farmland plot is a subrectangle of the grid where all the elements are 1s.
// The function returns a list of the top-left and bottom-right coordinates of each farmland plot.
//
// Parameters:
//  - land: A 2D integer array representing the grid.
//
// Returns:
//  - A 2D integer array where each element is a list of four integers [row1, col1, row2, col2]
//    that describes the top-left row1, col1 and bottom-right row2, col2 coordinates of a farmland plot.
//
// Error Handling:
//  - If the grid is empty or contains no farmland plots, the function returns an empty list.
//
// Example Usage:
//  land := [][]int{{1,0,0},{0,1,1},{0,1,1}}
//  farmlandPlots := findFarmland(land) // farmlandPlots now contains the coordinates of each farmland plot.
func findFarmland(land [][]int) [][]int {
	var list [][]int

	for i := 0; i < len(land); i++ {
		for j := 0; j < len(land[0]); j++ {
			if land[i][j] == 1 {
				arr := []int{i, j, 0, 0}
				dfs(land, i, j, arr)
				list = append(list, arr)
			}
		}
	}

	return list
}

// dfs is a helper function that performs a depth-first search on the grid starting from a given cell.
// It marks the visited cells and updates the bottom-right coordinates of the current farmland plot.
//
// Parameters:
//  - land: A 2D integer array representing the grid.
//  - i, j: The row and column indices of the current cell.
//  - arr: A list of four integers that describes the top-left and bottom-right coordinates of the current farmland plot.
//
// Returns:
//  - None. The function modifies the grid and the coordinates list in-place.
//
// Error Handling:
//  - If the current cell is out of bounds or is not part of a farmland plot, the function returns without doing anything.
func dfs(land [][]int, i, j int, arr []int) {
	if i >= len(land) || j >= len(land[0]) || land[i][j] == 0 {
		return
	}

	land[i][j] = 0
	arr[2] = max(i, arr[2])
	arr[3] = max(arr[3], j)

	dfs(land, i+1, j, arr)
	dfs(land, i, j+1, arr)
}

// max returns the maximum of two integers.
//
// Parameters:
//  - a, b: The two integers to compare.
//
// Returns:
//  - The maximum of a and b.
//
// Example Usage:
//  maximum := max(1, 2) // maximum now contains the value 2.
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
