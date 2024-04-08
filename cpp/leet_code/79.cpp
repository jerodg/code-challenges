class Solution {
public:
    bool dfs(vector <vector<char>> &board, int i, int j, string &word, int idx, vector <vector<bool>> &visited) {
        if (idx == word.size()) {
            return true;
        }
        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || visited[i][j] || board[i][j] != word[idx]) {
            return false;
        }
        visited[i][j] = true;
        bool ans = dfs(board, i + 1, j, word, idx + 1, visited) || dfs(board, i - 1, j, word, idx + 1, visited) ||
                   dfs(board, i, j + 1, word, idx + 1, visited) || dfs(board, i, j - 1, word, idx + 1, visited);
        visited[i][j] = false;
        return ans;
    }

    bool exist(vector <vector<char>> &board, string word) {
        int n = board.size();
        int m = board[0].size();
        vector <vector<bool>> visited(n, vector<bool>(m, false));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                bool ans = dfs(board, i, j, word, 0, visited);
                if (ans) {
                    return true;
                }
            }
        }
        return false;
    }
};