class Solution {
    func dfs(_ board: [[Character]], _ i: Int, _ j: Int, _ word: [Character], _ index: Int, _ visited: inout [[Bool]]) -> Bool {
        if index == word.count {
            return true
        }
        if i < 0 || i >= board.count || j < 0 || j >= board[0].count || visited[i][j] || board[i][j] != word[index] {
            return false
        }
        visited[i][j] = true
        let res = dfs(board, i + 1, j, word, index + 1, &visited) || dfs(board, i - 1, j, word, index + 1, &visited) || dfs(board, i, j + 1, word, index + 1, &visited) || dfs(board, i, j - 1, word, index + 1, &visited)
        visited[i][j] = false
        return res
    }

    func exist(_ board: [[Character]], _ word: String) -> Bool {
        let rows = board.count
        let cols = board[0].count
        var visited = Array(repeating: Array(repeating: false, count: cols), count: rows)
        let word = Array(word)
        for i in 0..<rows {
            for j in 0..<cols {
                if dfs(board, i, j, word, 0, &visited) {
                    return true
                }
            }
        }
        return false
    }
}