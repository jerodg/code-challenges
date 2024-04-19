#include <stdio.h>

/**
 * @file 200.c
 * @brief Contains the implementation of the number of islands problem.
 */

/**
 * @brief Performs a depth-first search (DFS) on the grid from a given cell.
 *
 * This function is used to mark the visited cells in the grid by changing their value to '0'.
 *
 * @param grid The 2D grid of cells.
 * @param i The row index of the current cell.
 * @param j The column index of the current cell.
 * @param rowSize The number of rows in the grid.
 * @param colSize The number of columns in the grid.
 * @return void
 */
void dfs(char **grid, int i, int j, int rowSize, int colSize) {
    // If the current cell is '0' (water), return.
    if (grid[i][j] == '0') return;

    // Mark the current cell as '0' (water).
    grid[i][j] = '0';

    // Perform DFS on the four adjacent cells if they are within the bounds of the grid.
    if (i + 1 < rowSize) dfs(grid, i + 1, j, rowSize, colSize);
    if (i - 1 >= 0) dfs(grid, i - 1, j, rowSize, colSize);
    if (j + 1 < colSize) dfs(grid, i, j + 1, rowSize, colSize);
    if (j - 1 >= 0) dfs(grid, i, j - 1, rowSize, colSize);
}

/**
 * @brief Counts the number of islands in the grid.
 *
 * An island is defined as a group of '1's (land) that are connected horizontally or vertically.
 * This function uses the DFS function to traverse the grid and count the number of islands.
 *
 * @param grid The 2D grid of cells.
 * @param gridSize The number of rows in the grid.
 * @param gridColSize The number of columns in the grid.
 * @return The number of islands in the grid.
 */
int numIslands(char **grid, int gridSize, int *gridColSize) {
    int ans = 0;

    // Traverse the grid.
    for (int i = 0; i < gridSize; ++i) {
        for (int j = 0; j < *gridColSize; ++j) {
            // If the current cell is '1' (land), perform DFS from here and increment the island count.
            if (grid[i][j] == '1') {
                ans++;
                dfs(grid, i, j, gridSize, *gridColSize);
            }
        }
    }

    return ans;
}

/**
 * @brief Example usage of the numIslands function.
 *
 * This function creates a grid and calls the numIslands function to count the number of islands in the grid.
 * The result is then printed to the standard output.
 *
 * @return void
 */
void exampleUsage() {
    // Create a 2D grid.
    char *grid[] = {"11000", "11000", "00100", "00011"};

    // Count the number of islands in the grid.
    int num_of_islands = numIslands(grid, 4, 5);

    // Print the result.
    printf("Number of islands: %d\n", num_of_islands);
}

int main() {
    exampleUsage();
    return 0;
}
