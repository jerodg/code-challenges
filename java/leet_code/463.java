import java.util.*;

/**
 * This class provides a solution for calculating the perimeter of an island in a 2D grid.
 * An island is defined as a group of '1's in the grid. Each group of '1's is surrounded by '0's.
 * The solution is to return the total perimeter of the island.
 */
class Solution {

    /**
     * Calculates the perimeter of an island in the given 2D grid.
     *
     * @param grid The 2D grid representing the land. '1's represent island and '0's represent water.
     * @return An integer representing the total perimeter of the island.
     */
    public int islandPerimeter(int[][] grid) {
        int height = grid.length;
        int width = grid[0].length;

        int result = 0;

        // Iterate over each row in the grid
        for (int y = 0; y < height; y++) {
            int prev = 0;
            // Iterate over each cell in the row
            for (int x = 0; x < width; x++) {
                int keep = grid[y][x];
                // If the current cell is part of the island and the previous cell is water, add 1 to the perimeter
                result += prev ^ keep;
                prev = keep;
            }
            // If the last cell in the row is part of the island, add 1 to the perimeter
            result += prev;
        }

        // Iterate over each column in the grid
        for (int x = 0; x < width; x++) {
            int prev = 0;
            // Iterate over each cell in the column
            for (int y = 0; y < height; y++) {
                int keep = grid[y][x];
                // If the current cell is part of the island and the previous cell is water, add 1 to the perimeter
                result += prev ^ keep;
                prev = keep;
            }
            // If the last cell in the column is part of the island, add 1 to the perimeter
            result += prev;
        }

        // Return the total perimeter of the island
        return result;
    }
}
