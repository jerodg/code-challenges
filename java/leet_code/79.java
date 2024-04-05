class Solution {
  public boolean exist(char[][] board, String word) {
    int m = board.length;
    int n = board[0].length;
    boolean[][] visited = new boolean[m][n];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        boolean res = dfs(board, i, j, word, 0, visited);
        if (res) {
          return true;
        }
      }
    }
    return false;
  }

  public boolean dfs(char[][] board, int i, int j, String word, int index, boolean[][] visited) {
    if (index == word.length()) {
      return true;
    }
    if (i < 0
        || i >= board.length
        || j < 0
        || j >= board[0].length
        || visited[i][j]
        || board[i][j] != word.charAt(index)) {
      return false;
    }
    visited[i][j] = true;
    boolean res =
        dfs(board, i + 1, j, word, index + 1, visited)
            || dfs(board, i - 1, j, word, index + 1, visited)
            || dfs(board, i, j + 1, word, index + 1, visited)
            || dfs(board, i, j - 1, word, index + 1, visited);
    visited[i][j] = false;
    return res;
  }
}
