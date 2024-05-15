import java.util.*;

/**
 * This class provides a solution for a problem related to finding the maximum safeness factor in a grid.
 * The grid is represented as a 2D list of integers.
 * <p>
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
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
class Solution {
    /**
     * This method calculates the maximum safeness factor in a given grid.
     *
     * @param grid The grid represented as a 2D list of integers.
     *
     * @return The maximum safeness factor as an integer.
     */
    public final int maximumSafenessFactor(final List<List<Integer>> grid) {
        final int n = grid.size();
        // If the first or last cell of the grid is 1, return 0 as the safeness factor.
        if ((grid.getFirst().getFirst() == 1) || (grid.get(n - 1).get(n - 1) == 1)) {
            return 0;
        }
        final int[][] cost = new int[n][n];
        for (final var v : cost) Arrays.fill(v, Integer.MAX_VALUE);
        this.bfs(cost, grid, n);
        int l = 1, r = n * n;
        int ans = 0;
        while (l <= r) {
            final int mid = (r - l) / 2 + l;
            if (this.possible(0, 0, cost, mid, n, new boolean[n][n])) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }
        return ans;
    }

    /**
     * This method checks if it's possible to reach the end of the grid with a given safeness factor.
     *
     * @param i       The current row in the grid.
     * @param j       The current column in the grid.
     * @param cost    The cost matrix.
     * @param mid     The current safeness factor.
     * @param n       The size of the grid.
     * @param visited A matrix to keep track of visited cells.
     *
     * @return True if it's possible to reach the end, false otherwise.
     */
    private boolean possible(final int i, final int j, final int[][] cost, final int mid, final int n, final boolean[][] visited) {
        if (i < 0 || j < 0 || i >= n || j >= n) return false;
        if (cost[i][j] == Integer.MAX_VALUE || cost[i][j] < mid) return false;
        if (i == n - 1 && j == n - 1) return true;
        if (visited[i][j]) return false;
        visited[i][j] = true;
        final int[][] dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        boolean ans = false;
        for (final var v : dir) {
            final int ii = i + v[0];
            final int jj = j + v[1];
            ans = this.possible(ii, jj, cost, mid, n, visited);
            if (ans) return true;
        }
        return false;
    }

    /**
     * This method performs a breadth-first search (BFS) on the grid to calculate the cost matrix.
     *
     * @param cost The cost matrix.
     * @param grid The grid represented as a 2D list of integers.
     * @param n    The size of the grid.
     */
    private void bfs(final int[][] cost, final List<? extends List<Integer>> grid, final int n) {
        final Queue<int[]> q = new LinkedList<>();
        final boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid.size(); j++) {
                if (grid.get(i).get(j) == 1) {
                    q.add(new int[]{i, j});
                    visited[i][j] = true;
                }
            }
        }
        int level = 1;
        final int[][] dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (!q.isEmpty()) {
            final int len = q.size();
            for (int i = 0; i < len; i++) {
                final var temp = q.poll();
                for (final var val : dir) {
                    final int ii = Objects.requireNonNull(temp)[0] + val[0];
                    final int jj = temp[1] + val[1];
                    if (Solution.isValid(ii, jj, n) && !visited[ii][jj]) {
                        q.add(new int[]{ii, jj});
                        cost[ii][jj] = Math.min(cost[ii][jj], level);
                        visited[ii][jj] = true;
                    }
                }
            }
            level++;
        }
    }

    /**
     * This method checks if a given cell is valid in the grid.
     *
     * @param i The row of the cell.
     * @param j The column of the cell.
     * @param n The size of the grid.
     *
     * @return True if the cell is valid, false otherwise.
     */
    private static boolean isValid(final int i, final int j, final int n) {
        return (i >= 0 && j >= 0 && i < n && j < n);
    }
}
