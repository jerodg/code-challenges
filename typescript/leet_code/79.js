/**
 * @fileoverview This module contains a solution for the "Word Search" problem from LeetCode.
 * The problem is solved by using a depth-first search (DFS) approach.
 */
/**
 * Function to check if the word exists in the grid.
 * @param {string[][]} board - The 2D grid of characters.
 * @param {string} word - The word to search for.
 * @return {boolean} True if the word exists in the grid, false otherwise.
 */
function exist(board, word) {
    var n = board.length;
    var m = board[0].length;
    /**
     * Helper function to perform depth-first search on the grid.
     * @param {number} i - The current row in the grid.
     * @param {number} j - The current column in the grid.
     * @param {number} k - The current character in the word.
     * @return {boolean} True if the word exists in the grid, false otherwise.
     */
    function dfs(i, j, k) {
        // Base case: if the current position is out of bounds or does not match the current character in the word
        if (i < 0 || i >= n || j < 0 || j >= m || board[i][j] !== word[k])
            return false;
        // If all characters in the word have been matched
        if (k === word.length - 1)
            return true;
        // Mark the current position as visited
        var temp = board[i][j];
        board[i][j] = "";
        // Perform DFS on the neighboring positions
        if (dfs(i - 1, j, k + 1) || dfs(i + 1, j, k + 1) || dfs(i, j - 1, k + 1) || dfs(i, j + 1, k + 1)) {
            // If the word exists, restore the current position and return true
            board[i][j] = temp;
            return true;
        }
        // If the word does not exist, restore the current position and return false
        board[i][j] = temp;
        return false;
    }
    // Iterate over each position in the grid
    for (var i = 0; i < n; i++) {
        for (var j = 0; j < m; j++) {
            // If the word exists starting from the current position, return true
            if (dfs(i, j, 0))
                return true;
        }
    }
    // If the word does not exist in the grid, return false
    return false;
}
