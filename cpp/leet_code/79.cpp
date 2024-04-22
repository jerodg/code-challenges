// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <string>
#include <vector>

class Solution {
public:
    bool dfs(std::vector <std::vector<char>> &board, int i, int j, std::string &word, int idx, std::vector <std::vector<bool>> &visited) {
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

    bool exist(std::vector <std::vector<char>> &board, std::string word) {
        int n = board.size();
        int m = board[0].size();
        std::vector <std::vector<bool>> visited(n, std::vector<bool>(m, false));
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
