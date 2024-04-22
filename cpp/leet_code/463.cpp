// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <vector>

// This class provides a solution for calculating the perimeter of an island in a grid.
class Solution {
public:
    // Method: islandPerimeter
    // This method calculates the perimeter of an island in a grid.
    //
    // Parameters:
    // grid - A 2D vector representing the grid. Each cell in the grid contains either a land (1) or a water (0).
    //
    // Returns:
    // The perimeter of the island.
    //
    // Example Usage:
    // Solution solution;
    // vector<vector<int>> grid = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
    // int perimeter = solution.islandPerimeter(grid);
    // cout << "Perimeter: " << perimeter << endl;
    //
    // Error Handling:
    // This method assumes that the input grid is well-formed and contains at least one cell.
    int islandPerimeter(std::vector<std::vector<int>> &grid) {
        int ans = 0;
        int n = grid.size();  // Number of rows in the grid
        int m = grid[0].size();  // Number of columns in the grid

        // Traverse each cell in the grid
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (grid[i][j] == 1) {  // If the cell is land
                    ans += 4;  // Add 4 to the perimeter for each land cell

                    // Subtract 2 from the perimeter for each adjacent land cell to the left
                    if (i > 0 && grid[i - 1][j] == 1) {
                        ans -= 2;
                    }

                    // Subtract 2 from the perimeter for each adjacent land cell above
                    if (j > 0 && grid[i][j - 1] == 1) {
                        ans -= 2;
                    }
                }
            }
        }

        return ans;  // Return the calculated perimeter
    }
};
