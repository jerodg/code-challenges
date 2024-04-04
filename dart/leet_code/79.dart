class Solution {
  dfs(List<List<String>> board, int i, int j, String word, int k) {
    if (i < 0 || j < 0 || i >= board.length || j >= board[i].length)
      return false;
    if (board[i][j] != word[k]) return false;
    if (k == word.length - 1) return true;
    var temp = board[i][j];
    board[i][j] = '';
    if (dfs(board, i + 1, j, word, k + 1) ||
        dfs(board, i - 1, j, word, k + 1) ||
        dfs(board, i, j + 1, word, k + 1) ||
        dfs(board, i, j - 1, word, k + 1)) {
      return true;
    }
    board[i][j] = temp;
    return false;
  }

  bool exist(List<List<String>> board, String word) {
    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[i].length; j++) {
        if (dfs(board, i, j, word, 0)) return true;
      }
    }
    return false;
  }
}
