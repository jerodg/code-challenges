public class Solution
{
    private bool dfs(char[][] board, int i, int j, int index, string word)
    {
        if (index == word.Length) return true;
        if (i < 0 || i >= board.Length || j < 0 || j >= board[i].Length || board[i][j] != word[index]) return false;
        char temp = board[i][j];
        board[i][j] = ' ';
        if (dfs(board, i + 1, j, index + 1, word) ||
            dfs(board, i - 1, j, index + 1, word) ||
            dfs(board, i, j + 1, index + 1, word) ||
            dfs(board, i, j - 1, index + 1, word))
        {
            return true;
        }

        board[i][j] = temp;
        return false;
    }

    public bool Exist(char[][] board, string word)
    {
        for (int i = 0; i < board.Length; i++)
        {
            for (int j = 0; j < board[i].Length; j++)
            {
                if (board[i][j] == word[0] && dfs(board, i, j, 0, word)) return true;
            }
        }

        return false;
    }
}