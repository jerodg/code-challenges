/**
 * This Kotlin module provides a solution for the LeetCode problem 79: Word Search.
 * The solution checks if the given word can be formed in the board by sequentially
 * adjacent cells, where "adjacent" cells are horizontally or vertically neighboring.
 *
 * @module leet_code/79.ws.kts
 */

/**
 * Solution class provides methods to check if a word can be formed in the board.
 */
class Solution {

    /**
     * This function checks if the given word can be formed in the board by sequentially
     * adjacent cells.
     *
     * @param board A 2D character array representing the board.
     * @param word A string representing the word to be searched in the board.
     * @return A boolean value indicating whether the word can be formed in the board or not.
     *
     * @throws IllegalArgumentException If the input board or word is null.
     *
     * Example usage:
     * val solution = Solution()
     * val board = arrayOf(charArrayOf('A','B','C','E'), charArrayOf('S','F','C','S'), charArrayOf('A','D','E','E'))
     * val word = "ABCCED"
     * val exists = solution.exist(board, word)
     * // exists will be true
     */
    fun exist(board: Array<CharArray>, word: String): Boolean {
        val m = board.size
        val n = board[0].size
        val visited = Array(m) { BooleanArray(n) }
        fun dfs(i: Int, j: Int, k: Int): Boolean {
            if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] || board[i][j] != word[k]) {
                return false
            }
            if (k == word.length - 1) {
                return true
            }
            visited[i][j] = true
            val res = dfs(i + 1, j, k + 1) || dfs(i - 1, j, k + 1) || dfs(i, j + 1, k + 1) || dfs(i, j - 1, k + 1)
            visited[i][j] = false
            return res
        }
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (dfs(i, j, 0)) {
                    return true
                }
            }
        }
        return false
    }
}
