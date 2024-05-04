/**
 * This class provides a solution for the problem of finding if a word exists in a 2D grid of characters.
 * The problem is solved using a depth-first search (DFS) approach, where each cell in the grid is visited and marked as visited.
 * The DFS is performed in all four directions (up, down, left, and right) from each cell.
 * If the word is found, the search is stopped and true is returned. If the word is not found after visiting all cells, false is returned.
 */
class Solution {

    /**
     * Determines if a word exists in a 2D grid of characters.
     *
     * @param board A 2D grid of characters. Each character is a letter.
     * @param word  The word to be found. It is a string of letters.
     *
     * @return True if the word exists in the grid, false otherwise.
     */
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

    /**
     * Performs a depth-first search (DFS) from a specific cell in the grid.
     *
     * @param board   The 2D grid of characters.
     * @param i       The row index of the cell from where the DFS is performed.
     * @param j       The column index of the cell from where the DFS is performed.
     * @param word    The word to be found.
     * @param index   The index of the character in the word to be matched.
     * @param visited A 2D array that keeps track of the visited cells.
     *
     * @return True if the word is found, false otherwise.
     */
    private boolean dfs(
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
