class Solution {
  public boolean exist(final char[][] board, final String word) {
    final int m = board.length;
    final int n = board[0].length;
    final boolean[][] visited = new boolean[m][n];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        final boolean res = this.dfs(board, i, j, word, 0, visited);
        if (res) {
          return true;
        }
      }
    }
    return false;
  }

  public boolean dfs(
      final char[][] board,
      final int i,
      final int j,
      final String word,
      final int index,
      final boolean[][] visited) {
    if (index == word.length()) {
      return true;
    }
    if (0 > i
        || i >= board.length
        || 0 > j
        || j >= board[0].length
        || visited[i][j]
        || board[i][j] != word.charAt(index)) {
      return false;
    }
    visited[i][j] = true;
    final boolean res =
        this.dfs(board, i + 1, j, word, index + 1, visited)
            || this.dfs(board, i - 1, j, word, index + 1, visited)
            || this.dfs(board, i, j + 1, word, index + 1, visited)
            || this.dfs(board, i, j - 1, word, index + 1, visited);
    visited[i][j] = false;
    return res;
  }
}
