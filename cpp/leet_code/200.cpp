#include <vector>  // For using vector

/**
 * @file 200.cpp
 * @brief Contains functions for counting the number of islands in a 2D grid.
 */

/**
 * @brief A Depth-First Search function to traverse the grid.
 *
 * This function traverses the grid in a depth-first manner. It marks the visited
 * cells as '0' to avoid revisiting them. The function recursively calls itself
 * for all four directions (up, down, left, right) from the current cell.
 *
 * @param grid The 2D grid represented as a double pointer.
 * @param i The current row index.
 * @param j The current column index.
 * @param rowSize The total number of rows in the grid.
 * @param colSize The total number of columns in the grid.
 */
void dfs(char **grid, int i, int j, int rowSize, int colSize) {
    if (grid[i][j] == '0') return;  // If the current cell is '0', return.
    grid[i][j] = '0';  // Mark the current cell as visited.

    // Recursively call dfs for all four directions.
    if (i + 1 < rowSize) dfs(grid, i + 1, j, rowSize, colSize);
    if (i - 1 >= 0) dfs(grid, i - 1, j, rowSize, colSize);
    if (j + 1 < colSize) dfs(grid, i, j + 1, rowSize, colSize);
    if (j - 1 >= 0) dfs(grid, i, j - 1, rowSize, colSize);
}

/**
 * @brief Function to count the number of islands in a 2D grid.
 *
 * This function counts the number of islands in a 2D grid. An island is
 * surrounded by water and is formed by connecting adjacent lands horizontally
 * or vertically. The function uses the dfs function to traverse the grid.
 *
 * @param grid The 2D grid represented as a double pointer.
 * @param gridSize The total number of rows in the grid.
 * @param gridColSize The total number of columns in the grid.
 * @return The number of islands in the grid.
 */
int numIslands(char **grid, int gridSize, int *gridColSize) {
    int ans = 0;  // Initialize the count of islands as 0.

    // Traverse the entire grid.
    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < *gridColSize; ++j) {
            // If the current cell is '1', increment the count of islands and call dfs.
            if (grid[i][j] == '1') {
                ans++;
                dfs(grid, i, j, gridSize, *gridColSize);
            }
        }
    }
    return ans;  // Return the count of islands.
}
