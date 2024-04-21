/**
 * @file 1992.cpp
 * @brief Contains the implementation of the Solution class.
 *
 * This file contains the implementation of a Solution class which provides a method to find farmland in a given land matrix.
 */

#include <ios> // For std::ios_base::sync_with_stdio
#include <iostream> // For std::cin.tie
#include <vector> // For std::vector

/**
 * @class Solution
 * @brief A class providing a method to find farmland in a given land matrix.
 *
 * This class provides a method to find farmland in a given land matrix. The farmland is represented by a 1 in the matrix and
 * each farmland is a rectangle. The method returns the top-left and bottom-right coordinates of each farmland.
 */
class Solution {
public:
    /**
     * @brief Finds the farmland in a given land matrix.
     *
     * This method finds the farmland in a given land matrix. The farmland is represented by a 1 in the matrix and each farmland is a rectangle.
     * The method returns the top-left and bottom-right coordinates of each farmland.
     *
     * @param land The land matrix.
     * @return A vector of vectors where each inner vector contains the top-left and bottom-right coordinates of a farmland.
     */
    std::vector<std::vector<int> > findFarmland(std::vector<std::vector<int> > &land) {
        std::ios_base::sync_with_stdio(false); // Speeds up I/O operations
        std::cin.tie(nullptr); // Unties cin from cout

        const int n = land.size(); // The number of rows in the land matrix
        const int m = land[0].size(); // The number of columns in the land matrix
        std::vector<std::vector<int> > result; // The result vector

        // Iterate over the land matrix
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!land[i][j]) continue; // If the current cell is not a farmland, continue to the next cell

                int c2 = j;
                // Find the right boundary of the farmland
                while (c2 < m && land[i][c2]) {
                    c2++;
                }
                int r2 = i;
                // Find the bottom boundary of the farmland
                while (r2 < n && land[r2][j]) {
                    r2++;
                }
                c2 = !c2 ? c2 : c2 - 1;
                r2 = !r2 ? r2 : r2 - 1;
                result.push_back({i, j, r2, c2}); // Add the farmland to the result

                // Mark the cells of the farmland as visited
                for (int k = i; k <= r2; k++) {
                    for (int l = j; l <= c2; l++) {
                        land[k][l] = 0;
                    }
                }
            }
        }
        return result; // Return the result
    }
};
