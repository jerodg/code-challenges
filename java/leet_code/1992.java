import java.util.*;

/**
 * This class provides a solution for finding all farmlands in a given 2D grid.
 * A farmland is defined as a group of '1's in the grid. Each group of '1's is
 * surrounded by '0's and forms a rectangle. The solution is to return the
 * coordinates of the top-left and bottom-right corners of each farmland.
 */
class Solution {

    /**
     * Finds all farmlands in the given 2D grid.
     *
     * @param land The 2D grid representing the land. '1's represent farmland and '0's represent non-farmland.
     * @return A 2D array where each element is an array of four integers representing the coordinates of the top-left and bottom-right corners of a farmland.
     */
    public int[][] findFarmland(int[][] land) {
        List<int[]> result = new ArrayList<>();

        int m = land.length;
        int n = land[0].length;

        // Iterate over the entire grid
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // If the current cell is farmland ('1'), find its coordinates
                if (land[i][j] == 1) {
                    int[] coordinates = findFarmlandCoordinates(land, i, j);
                    result.add(coordinates);
                }
            }
        }

        // Convert the result to a 2D array
        return result.toArray(new int[result.size()][]);
    }

    /**
     * Finds the coordinates of the farmland that includes the given cell.
     *
     * @param land The 2D grid representing the land.
     * @param row The row index of the given cell.
     * @param col The column index of the given cell.
     * @return An array of four integers representing the coordinates of the top-left and bottom-right corners of the farmland.
     */
    private int[] findFarmlandCoordinates(int[][] land, int row, int col) {
        int[] coordinates = new int[4];
        coordinates[0] = row;
        coordinates[1] = col;

        int m = land.length;
        int n = land[0].length;

        int r = row;
        int c = col;

        // Find the bottom-right corner of the farmland group
        while (r < m && land[r][col] == 1) r++;
        while (c < n && land[row][c] == 1) c++;
        coordinates[2] = r - 1;
        coordinates[3] = c - 1;

        // Mark all cells in the farmland group as visited ('0')
        for (int i = row; i < r; i++) {
            for (int j = col; j < c; j++) {
                land[i][j] = 0;
            }
        }

        return coordinates;
    }
}
