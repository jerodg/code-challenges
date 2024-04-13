/**
 * Function to determine if a word exists in a 2D board
 * Each word must be constructed from letters of sequentially adjacent cells,
 * where "adjacent" cells are horizontally or vertically neighboring.
 * The same letter cell may not be used more than once.
 *
 * @param {character[][]} board - 2D array of characters
 * @param {string} word - Word to be found in the board
 * @returns {boolean} - True if the word can be found, false otherwise
 */
const exist = function (board, word) {
    const m = board.length;
    const n = board[0].length;

    // Create a 2D array to keep track of visited cells
    const visited = new Array(m).fill(0).map(() => {
        return new Array(n).fill(false);
    });

    /**
     * Depth-first search function to find the word in the board
     *
     * @param {number} x - Current row index
     * @param {number} y - Current column index
     * @param {number} idx - Current index in the word
     * @returns {boolean} - True if the word can be found, false otherwise
     */
    const dfs = (x, y, idx) => {
        // If the entire word has been found
        if (idx === word.length) {
            return true;
        }

        // If the current cell is out of bounds, already visited, or does not match the current character in the word
        if (x < 0 || x >= m || y < 0 || y >= n || visited[x][y] || board[x][y] !== word[idx]) {
            return false;
        }

        // Mark the current cell as visited
        visited[x][y] = true;

        // Define the four possible directions to move in the board
        const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];

        // Try each direction
        for (const [dx, dy] of directions) {
            if (dfs(x + dx, y + dy, idx + 1)) {
                return true;
            }
        }

        // If the word cannot be found, backtrack by marking the current cell as not visited
        visited[x][y] = false;

        return false;
    };

    // Try to find the word starting from each cell in the board
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (dfs(i, j, 0)) {
                return true;
            }
        }
    }

    // If the word cannot be found in the board
    return false;
};
