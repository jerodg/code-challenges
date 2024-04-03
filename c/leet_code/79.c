bool exist(char **board, int boardSize, int *boardColSize, char *word) {
    int m = boardSize;
    int n = *boardColSize;
    int len = strlen(word);
    if (m == 0 || n == 0) {
        return false;
    }
    if (len == 0) {
        return true;
    }
    int **visited = (int **) malloc(m * sizeof(int *));
    for (int i = 0; i < m; i++) {
        visited[i] = (int *) calloc(n, sizeof(int));
    }
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (dfs(board, visited, i, j, m, n, word, 0)) {
                for (int i = 0; i < m; i++) {
                    free(visited[i]);
                }
                free(visited);
                return true;
            }
        }
    }
    for (int i = 0; i < m; i++) {
        free(visited[i]);
    }
    free(visited);
    return false;
}

int dfs(char **board, int **visited, int i, int j, int m, int n, char *word, int index) {
    if (i < 0 || i >= m || j < 0 || j >= n || visited[i][j] || board[i][j] != word[index]) {
        return 0;
    }
    if (index == strlen(word) - 1) {
        return 1;
    }
    visited[i][j] = 1;
    int res = dfs(board, visited, i + 1, j, m, n, word, index + 1) ||
              dfs(board, visited, i - 1, j, m, n, word, index + 1) ||
              dfs(board, visited, i, j + 1, m, n, word, index + 1) ||
              dfs(board, visited, i, j - 1, m, n, word, index + 1);
    visited[i][j] = 0;
    return res;
}