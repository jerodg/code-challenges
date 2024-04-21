// Package leet_code provides solutions for LeetCode problems.
package leet_code

// islandPerimeter calculates the perimeter of the island in a grid.
// The grid is represented as a 2D array where 0 represents water and 1 represents land.
// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
// The function assumes that all four edges of the grid are surrounded by water.
//
// Parameters:
//  - grid: A 2D integer array representing the grid.
//
// Returns:
//  - The perimeter of the island.
//
// Error Handling:
//  - If the grid is empty, the function returns 0.
//
// Example Usage:
//  grid := [][]int{{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}}
//  perimeter := islandPerimeter(grid) // perimeter now contains the perimeter of the island.
func islandPerimeter(grid [][]int) int {
	// Directions for exploring the neighbors of a cell
	DIRS := [][]int{{-1, 0}, {0, -1}, {1, 0}, {0, 1}}
	sides := 0

	// Iterate over each cell in the grid
	for row, ROWS := 0, len(grid); row < ROWS; row++ {
		for col, COLS := 0, len(grid[0]); col < COLS; col++ {
			// If the cell is land
			if grid[row][col] == 1 {
				// Check each neighbor of the cell
				for _, dir := range DIRS {
					r, c := row+dir[0], col+dir[1]
					// If the neighbor is out of bounds or is water, increment the perimeter
					if r < 0 || r >= ROWS || c < 0 || c >= COLS || grid[r][c] == 0 {
						sides++
					}
				}
			}
		}
	}
	// Return the calculated perimeter
	return sides
}
