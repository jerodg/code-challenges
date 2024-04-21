/**
 * @file leet_code/1992.c
 * @brief This file contains the implementation of the findFarmland function.
 *
 * The function finds all farmlands in a given 2D grid. A farmland is a group of 1s that are 4-directionally adjacent.
 * The function returns the coordinates of the top-left and bottom-right corners of each farmland.
 * The coordinates are represented as 4-element arrays [r1, c1, r2, c2], where r1 and c1 are the coordinates of the top-left corner,
 * and r2 and c2 are the coordinates of the bottom-right corner.
 * The function uses a breadth-first search algorithm to traverse the grid.
 */

#include <stdlib.h>  // Required for dynamic memory allocation functions

/**
 * @brief Finds all farmlands in a given 2D grid.
 *
 * This function uses a breadth-first search algorithm to traverse the grid.
 * It starts from each unvisited cell that contains a 1 and explores all its 4-directionally adjacent cells that also contain a 1.
 * The coordinates of the top-left and bottom-right corners of each farmland are stored in a 2D array.
 *
 * @param land 2D array representing the grid.
 * @param landSize Number of rows in the grid.
 * @param landColSize Array representing the number of columns in each row of the grid.
 * @param returnSize Pointer to an integer where the number of farmlands will be stored.
 * @param returnColumnSizes Pointer to a 1D array where the number of columns in each row of the return array will be stored.
 * @return 2D array containing the coordinates of the top-left and bottom-right corners of each farmland.
 *         The caller is responsible for freeing this memory when it's no longer needed.
 * @throws This function does not throw any exceptions.
 */
int **findFarmland(int **land, const int landSize, const int *landColSize, int *returnSize, int **returnColumnSizes) {
    const int m = landSize;
    const int n = landColSize[0];
    int *seen = calloc(sizeof(int), m * n); // Array to keep track of visited cells
    int **groups = calloc(sizeof(int *), (m * n + 1) / 2); // Array to store the coordinates of each farmland
    *returnColumnSizes = calloc(sizeof(int), (m * n + 1) / 2);
    // Array to store the number of columns in each row of the return array
    *returnSize = 0; // Initialize the number of farmlands to 0

    // Traverse the grid
    for (int r1 = 0; r1 < m; r1++) {
        for (int c1 = 0; c1 < n; c1++) {
            // If the current cell contains a 1 and has not been visited yet, start a new farmland
            if ((seen[r1 * n + c1] == 0) && (land[r1][c1] == 1)) {
                int c2 = c1;
                // Find the rightmost cell of the farmland
                while ((c2 + 1 < n) && (land[r1][c2 + 1] == 1)) { c2++; }

                int r2 = r1;
                // Find the bottommost cell of the farmland
                while ((r2 + 1 < m) && (land[r2 + 1][c1] == 1)) { r2++; }

                // Store the coordinates of the farmland
                (*returnColumnSizes)[*returnSize] = 4;
                groups[*returnSize] = calloc(sizeof(int), 4);
                groups[*returnSize][0] = r1;
                groups[*returnSize][1] = c1;
                groups[*returnSize][2] = r2;
                groups[*returnSize][3] = c2;
                (*returnSize)++;

                // Mark all cells of the farmland as visited
                for (int i = r1; i <= r2; i++) {
                    for (int j = c1; j <= c2; j++) {
                        seen[i * n + j] = 1;
                    }
                }
            }
        }
    }
    free(seen); // Free the memory allocated for the seen array
    return groups; // Return the coordinates of the farmlands
}
