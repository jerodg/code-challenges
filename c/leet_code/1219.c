/**
 * @file leet_code/1219.c
 * @brief This file contains the implementation of functions to solve a problem related to a grid.
 *
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */

#pragma GCC optimize("O3,unroll-loops")

/**
 * @brief Global variables to store the number of rows and columns in the grid, and the maximum gold that can be collected.
 */
int row = 0;
int col = 0;
int ans = 0;

/**
 * @brief A 2D array to store the possible directions to move in the grid.
 */
const int dirs[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

/**
 * @brief Checks if all cells in the grid are non-zero and updates the global variable 'ans' with the sum of all cells.
 *
 * @param grid The 2D grid.
 * @return int Returns the sum of all cells if all are non-zero, otherwise returns 0.
 */
int checkIfAllNonZero(int** grid) {
    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            switch (grid[i][j]) {
                case 0: ans = 0; return 0;
                default: ans += grid[i][j];
            }
        }
    }
    return ans;
}

/**
 * @brief Performs a depth-first search (DFS) on the grid from a given cell, and updates the global variable 'ans' with the maximum gold that can be collected.
 *
 * @param grid The 2D grid.
 * @param i The row index of the current cell.
 * @param j The column index of the current cell.
 * @param tmp The gold collected so far.
 */
void dfs(int** grid, int i, int j, int tmp) {
    int num = grid[i][j];
    grid[i][j] = 0;
    tmp += num;

    bool flag = false;
    for (int k = 0; k < 4; ++k) {
        int x = dirs[k][0] + i;
        int y = dirs[k][1] + j;

        if (x >= row || x < 0 || y >= col || y < 0 || grid[x][y] == 0) {
            continue;
        }

        flag = true;
        dfs(grid, x, y, tmp);
    }

    if (!flag) {
        ans = (ans > tmp) ? ans : tmp;
    }

    grid[i][j] = num;
}

/**
 * @brief Computes the maximum gold that can be collected from the grid.
 *
 * @param grid The 2D grid.
 * @param gridSize The number of rows in the grid.
 * @param gridColSize The number of columns in the grid.
 * @return int The maximum gold that can be collected.
 */
int getMaximumGold(int** grid, int gridSize, const int* gridColSize) {
    row = gridSize;
    col = gridColSize[0];
    ans = 0;

    if (checkIfAllNonZero(grid) != 0) {
        return ans;
    }

    for (int i = 0; i < row; ++i) {
        for (int j = 0; j < col; ++j) {
            if (grid[i][j] != 0) {
                dfs(grid, i, j, 0);
            }
        }
    }
    return ans;
}
