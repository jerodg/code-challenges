/**
 An `Solution` class that calculates the perimeter of an island in a grid.

 The grid is represented as a 2D array, where 0 represents water and 1 represents land. The grid cells are connected horizontally and vertically but not diagonally. The perimeter of the island is the total number of land-to-water or land-to-grid-edge transitions.

 - Note: The grid is assumed to be rectangular, with the same number of columns in each row.
 */
import Foundation

class Solution {
    /**
     Calculates the perimeter of the island in the given grid.

     This method traverses the grid from top to bottom and left to right. For each land cell, it adds 4 to the perimeter (since a standalone cell has 4 sides). Then, if the cell has a neighbor to the right or down that is also a land cell, it subtracts 2 from the perimeter (since each shared side between two cells reduces the total perimeter by 2).

     - Parameter grid: A 2D array representing the grid. Each element is either 0 (water) or 1 (land).
     - Returns: The total perimeter of the island in the grid.
     - Throws: This method does not throw any error.
     - Precondition: The grid is non-empty and rectangular, with the same number of columns in each row.
     - Postcondition: The returned value is non-negative and represents the total perimeter of the island in the grid.

     - Example:
     ```
     let solution = Solution()
     let grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
     let perimeter = solution.islandPerimeter(grid)
     print(perimeter)  // Prints "16"
     ```
     */
    func islandPerimeter(_ grid: [[Int]]) -> Int {
        let rows = grid.count
        let columns = grid[0].count

        var perimeter = 0

        for i in 0 ..< rows {
            for j in 0 ..< columns {
                if grid[i][j] == 1 {
                    perimeter += 4

                    // Check the cell below
                    if i < rows - 1, grid[i + 1][j] == 1 {
                        perimeter -= 2
                    }

                    // Check the cell to the right
                    if j < columns - 1, grid[i][j + 1] == 1 {
                        perimeter -= 2
                    }
                }
            }
        }

        return perimeter
    }
}
