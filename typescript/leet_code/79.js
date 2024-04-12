function exist(board, word) {
    var n = board.length;
    var m = board[0].length;
    function dfs(i, j, k) {
        if (i < 0 || i >= n || j < 0 || j >= m || board[i][j] !== word[k])
            return false;
        if (k === word.length - 1)
            return true;
        var temp = board[i][j];
        board[i][j] = "";
        if (dfs(i - 1, j, k + 1) || dfs(i + 1, j, k + 1) || dfs(i, j - 1, k + 1) || dfs(i, j + 1, k + 1)) {
            board[i][j] = temp;
            return true;
        }
        board[i][j] = temp;
        return false;
    }
    for (var i = 0; i < n; i++) {
        for (var j = 0; j < m; j++) {
            if (dfs(i, j, 0))
                return true;
        }
    }
    return false;
}
