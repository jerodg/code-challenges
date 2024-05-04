import java.util.LinkedList;
import java.util.Queue;

/**
 * Solution class for LeetCode problem 200: Number of Islands.
 *
 * <p>This class provides a method to count the number of islands in a 2D grid map. An island is
 * surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You
 * may assume all four edges of the grid are all surrounded by water.
 *
 * <p>Example usage:
 * <pre>
 *   Solution solution = new Solution();
 *   char[][] grid = {{'1','1','1','1','0'}, {'1','1','0','1','0'}, {'1','1','0','0','0'}, {'0','0','0','0','0'}};
 *   int numberOfIslands = solution.numIslands(grid);
 *   System.out.println(numberOfIslands);  // Outputs: 1
 * </pre>
 */
class Solution {

    /**
     * Counts the number of islands in the given 2D grid map.
     *
     * @param grid the 2D grid map of '1's (land) and '0's (water)
     *
     * @return the number of islands
     *
     * @throws NullPointerException if grid is null
     */
    public int numIslands(final char[][] grid) {
        if (grid == null || grid.length == 0) {
            throw new NullPointerException("Grid cannot be null or empty");
        }

        final int rows = grid.length;
        final int cols = grid[0].length;
        int numberOfIslands = 0;

        // Iterate over the entire grid
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                // If the current cell is land ('1'), start a new island
                if ((int) '1' == (int) grid[row][col]) {
                    numberOfIslands++;
                    grid[row][col] = '0'; // mark the current cell as visited
                    final Queue<int[]> neighbours = new LinkedList<>();
                    neighbours.add(new int[]{row, col});

                    // Perform BFS to visit all cells in the current island
                    while (!neighbours.isEmpty()) {
                        final int[] id = neighbours.remove();
                        final int r = id[0];
                        final int c = id[1];

                        // Check the four directions around the current cell
                        if (0 <= r - 1 && '1' == (int) grid[r - 1][c]) {
                            neighbours.add(new int[]{r - 1, c});
                            grid[r - 1][c] = '0';
                        }
                        if (r + 1 < rows && (int) '1' == (int) grid[r + 1][c]) {
                            neighbours.add(new int[]{r + 1, c});
                            grid[r + 1][c] = '0';
                        }
                        if (0 <= c - 1 && (int) '1' == (int) grid[r][c - 1]) {
                            neighbours.add(new int[]{r, c - 1});
                            grid[r][c - 1] = '0';
                        }
                        if (c + 1 < cols && (int) '1' == (int) grid[r][c + 1]) {
                            neighbours.add(new int[]{r, c + 1});
                            grid[r][c + 1] = '0';
                        }
                    }
                }
            }
        }

        return numberOfIslands;
    }
}
