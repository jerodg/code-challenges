/**
 * Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
 * <p>
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 * <p>
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 * <p>
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * This class provides a solution for a specific problem from LeetCode.
 * The problem is about maximizing the score of a binary matrix by flipping rows and columns.
 */
class Solution {
    /**
     * This method calculates the maximum score that can be obtained from a binary matrix.
     * The score is calculated by considering each row as a binary number and summing them up.
     * The method first flips the rows to make sure the leftmost column is all 1s, as this maximizes the score.
     * Then, for each column, it counts the number of 1s and 0s and flips the column if there are more 0s than 1s.
     *
     * @param grid The binary matrix represented as a 2D integer array.
     * @return The maximum score that can be obtained from the binary matrix.
     */
    public static int matrixScore(final int[][] grid) {
        final int n = grid.length;
        final int m = grid[0].length;
        // Initialize the result with the score contributed by the first column.
        int res = (1 << (m - 1)) * n;

        // Iterate over the rest of the columns.
        for (int j = 1; j < m; ++j) {
            final int val = 1 << (m - 1 - j);
            int set = 0;

            // Count the number of 1s in the column.
            for (final int[] ints : grid) {
                if (ints[j] == ints[0]) {
                    set++;
                }
            }
            // Add the maximum possible score from the column to the result.
            res += Math.max(set, n - set) * val;
        }
        return res;
    }
}
