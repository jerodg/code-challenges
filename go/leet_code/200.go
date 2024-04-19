// Package leet_code provides solutions for LeetCode problems.
package leet_code

// dfs is a helper function that performs a depth-first search on the board.
// It checks if the word exists in the board starting from the cell at (i, j).
//
// Parameters:
//  - board: 2D byte array representing the board.
//  - i: Row index of the starting cell.
//  - j: Column index of the starting cell.
//  - word: The word to be searched.
//  - k: The index of the character in the word to be matched.
//
// Returns:
//  - true if the word is found, false otherwise.
//
// Example:
//  board := [][]byte{{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}}
//  word := "ABCCED"
//  result := dfs(board, 0, 0, word, 0) // result: true
func dfs(board [][]byte, i, j int, word string, k int) bool {
	if i < 0 || i >= len(board) || j < 0 || j >= len(board[i]) {
		return false
	}

	if board[i][j] != word[k] {
		return false
	}

	if k == len(word)-1 {
		return true
	}

	tmp := board[i][j]
	board[i][j] = '.'

	if dfs(board, i-1, j, word, k+1) || dfs(board, i+1, j, word, k+1) || dfs(board, i, j-1, word, k+1) || dfs(board, i, j+1, word, k+1) {
		return true
	}

	board[i][j] = tmp

	return false
}

// exist checks if the word exists in the board.
//
// Parameters:
//  - board: 2D byte array representing the board.
//  - word: The word to be searched.
//
// Returns:
//  - true if the word is found, false otherwise.
//
// Example:
//  board := [][]byte{{'A','B','C','E'},{'S','F','C','S'},{'A','D','E','E'}}
//  word := "ABCCED"
//  result := exist(board, word) // result: true
func exist(board [][]byte, word string) bool {
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[i]); j++ {
			if dfs(board, i, j, word, 0) {
				return true
			}
		}
	}

	return false
}

// numIslands counts the number of islands in the grid.
//
// Parameters:
//  - grid: 2D byte array representing the grid.
//
// Returns:
//  - The number of islands in the grid.
//
// Example:
//  grid := [][]byte{{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}}
//  result := numIslands(grid) // result: 1
func numIslands(grid [][]byte) int {
	if grid == nil {
		return 0
	}
	var res int
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			res += findIsl(i, j, grid)
		}
	}
	return res
}

// findIsl is a helper function that finds an island in the grid.
//
// Parameters:
//  - i: Row index of the starting cell.
//  - j: Column index of the starting cell.
//  - m: 2D byte array representing the grid.
//
// Returns:
//  - 1 if an island is found, 0 otherwise.
//
// Example:
//  i := 0
//  j := 0
//  m := [][]byte{{'1','1','1','1','0'},{'1','1','0','1','0'},{'1','1','0','0','0'},{'0','0','0','0','0'}}
//  result := findIsl(i, j, m) // result: 1
func findIsl(i, j int, m [][]byte) int {
	if i == -1 || j == -1 || i == len(m) || j == len(m[0]) {
		return 0
	}
	if m[i][j] == '1' {
		m[i][j] = '0'
		findIsl(i-1, j, m)
		findIsl(i+1, j, m)
		findIsl(i, j+1, m)
		findIsl(i, j-1, m)
		return 1
	}
	return 0
}
