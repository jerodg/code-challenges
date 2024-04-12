/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */

const exist = function (board, word) {
    const m = board.length;
    const n = board[0].length;
    const visited = new Array(m).fill(0).map(() => {
        return new Array(n).fill(false);
    });
    const dfs = (x, y, idx) => {
        if (idx === word.length) {
            return true;
        }
        if (x < 0 || x >= m || y < 0 || y >= n || visited[x][y] || board[x][y] !== word[idx]) {
            return false;
        }
        visited[x][y] = true;
        const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
        for (const [dx, dy] of directions) {
            if (dfs(x + dx, y + dy, idx + 1)) {
                return true;
            }
        }
        visited[x][y] = false;
        return false;
    };
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (dfs(i, j, 0)) {
                return true;
            }
        }
    }
    return false;
};
