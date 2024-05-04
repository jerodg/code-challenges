// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of determining if a word exists in a 2D grid of characters.
// The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring.
// The same letter cell may not be used more than once.
package leet_code

// dfs is a helper function that performs a depth-first search on the board starting from the cell at (i, j).
//
// It accepts five parameters:
// - board: a 2D byte array representing the board.
// - i, j: integers representing the starting cell coordinates.
// - word: a string representing the word to be found.
// - k: an integer representing the current character of the word.
//
// The function returns a boolean indicating whether the word can be found starting from the cell at (i, j).
//
// The function checks the current cell and recursively checks its adjacent cells.
//
// Time complexity analysis:
// - Best-case: O(1), when the word is found in the first cell.
// - Worst-case: O(m*n*4^k), where m and n are the dimensions of the board and k is the length of the word.
// - Average-case: O(m*n*4^k), as in the worst case.
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

// exist determines if a word exists in a 2D grid of characters.
//
// It accepts two parameters:
// - board: a 2D byte array representing the board.
// - word: a string representing the word to be found.
//
// The function returns a boolean indicating whether the word exists in the board.
//
// The function iterates over the board and for each cell, it calls the dfs function to check if the word exists starting from that cell.
//
// Time complexity analysis:
// - Best-case: O(1), when the word is found in the first cell.
// - Worst-case: O(m*n*4^k), where m and n are the dimensions of the board and k is the length of the word.
// - Average-case: O(m*n*4^k), as in the worst case.
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
