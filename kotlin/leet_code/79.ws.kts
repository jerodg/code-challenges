class Solution {
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