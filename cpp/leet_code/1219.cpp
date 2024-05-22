/**
 * @file 1219.cpp
 * @brief This file contains the implementation of a solution for a problem related to finding the maximum gold in a grid.
 * @details The grid is represented as a 2D vector. Each cell in the grid represents a gold mine with a certain amount of gold.
 * The goal is to find the maximum amount of gold that can be collected by moving from one cell to another.
 * The movement is allowed only to the adjacent cells and once a cell is visited, it cannot be visited again.
 * The solution uses depth-first search (DFS) to explore all possible paths and keeps track of the maximum gold collected.
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

 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */

#ifndef OUT
#define OUT(...)
#endif
#include <cassert>
#include <vector>

// nxt and val are global arrays used to store the next cell to visit and the value of the current cell respectively.
int nxt[40];
int val[40];

/**
 * @brief This function performs a depth-first search on the grid starting from a given cell.
 * @param r The row index of the current cell.
 * @param c The column index of the current cell.
 * @param cnt The count of cells visited so far.
 * @param sum The total amount of gold collected so far.
 * @param grid The 2D vector representing the grid.
 * @param ids A 2D vector used to keep track of the cells that have been visited.
 */
void dfs1(int r, int c, int &cnt, int &sum, const std::vector<std::vector<int>> &grid, std::vector<std::vector<int>> &ids) {
    constexpr std::pair<int, int> idx[] = {
            {0,  1},
            {1,  0},
            {0,  -1},
            {-1, 0},
    };
    assert(grid[r][c] > 0);
    assert(ids[r][c] < 0);
    const int cur = ids[r][c] = cnt++;
    nxt[cur] = 0;
    val[cur] = grid[r][c];
    sum += val[cur];
    for (const auto & [fst, snd]: idx) {
        const int rr = r + fst ;const int cc = c + snd;
        if (rr < 0 || rr >= static_cast<int>(grid.size())) continue;
        if (cc < 0 || cc >= static_cast<int>(grid[rr].size())) continue;
        if (!grid[rr][cc]) continue;
        if (ids[rr][cc] < 0) dfs1(rr, cc, cnt, sum, grid, ids);
        nxt[cur] |= 1 << ids[rr][cc];
    }
}

int currentMax, sum; // currentMax and sum are global variables used to keep track of the maximum gold collected and the total gold collected so far respectively.

/**
 * @brief This function performs a depth-first search on the grid to find the maximum gold that can be collected.
 * @param s The total amount of gold collected so far.
 * @param cur The current cell.
 * @param rem The remaining cells to visit.
 */
auto dfs2(int s, const int cur, int rem)-> void {
    s += val[cur];
    currentMax = std::max(s, currentMax);
    if (currentMax == sum) return;
    rem &= ~(1 << cur);

    for (int p = nxt[cur] & rem; p; p &= p - 1) {
        const int bit = p & -p;
        const int i = __builtin_ctz(bit);
        dfs2(s, i, rem);
    }
}

/**
 * @brief This function finds the maximum gold that can be collected starting from a given cell.
 * @param grid The 2D vector representing the grid.
 * @param ids A 2D vector used to keep track of the cells that have been visited.
 * @param r The row index of the starting cell.
 * @param c The column index of the starting cell.
 * @return The maximum gold that can be collected.
 */
int solve(const std::vector<std::vector<int>> &grid, std::vector<std::vector<int>> &ids, const int r, const int c) {
    int cnt = 0;
    sum = 0;
    dfs1(r, c, cnt, sum, grid, ids);
    OUT(cnt, sum);
    OUT(vector(val, val + cnt));
    OUT(vector(nxt, nxt + cnt));
    const int mask = (1 << cnt) - 1;
    currentMax = 0;
    for (int i = 0; i < cnt; ++i) {
        dfs2(0, i, mask);
    }
    return currentMax;
}

/**
 * @class Solution
 * @brief This class encapsulates the solution for the problem.
 */
class Solution {
public:
    /**
     * @brief This function finds the maximum gold that can be collected from the grid.
     * @param grid The 2D vector representing the grid.
     * @return The maximum gold that can be collected.
     */
    static int getMaximumGold(const std::vector<std::vector<int>> &grid) {
        const int m = static_cast<int>(grid.size());
        const int n = static_cast<int>(grid[0].size());
        int ans = 0;
        std::vector<std::vector<int> > ids(m, std::vector<int>(n, -1));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (ids[i][j] >= 0) continue;
                if (!grid[i][j]) continue;
                ans = std::max(ans, solve(grid, ids, i, j));
            }
        }
        return ans;
    }
};
