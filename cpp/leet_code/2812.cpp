/**
 * @file leet_code/2812.cpp
 * @brief This file contains the Solution class which is used to solve the problem of finding the maximum safeness factor in a grid.
 * @copyright Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */

#pragma GCC optimize("O3,unroll-loops")

#include <climits>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

/**
 * @class Solution
 * @brief This class is used to solve the problem of finding the maximum safeness factor in a grid.
 */
class Solution {
  public:
    /**
     * @brief These vectors are used to navigate the grid in four directions: up, down, left, and right.
     */
    vector<int> roww = {0, 0, -1, 1};
    vector<int> coll = {-1, 1, 0, 0};

    /**
     * @brief This method performs a breadth-first search (BFS) on the grid to find the shortest path from each cell to the nearest obstacle.
     * @param grid The grid on which the BFS is performed.
     * @param score The matrix that stores the shortest path from each cell to the nearest obstacle.
     * @param n The size of the grid.
     */
    void bfs(vector<vector<int>>& grid, vector<vector<int>>& score, int n) {
        queue<pair<int, int>> q;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j]) {
                    score[i][j] = 0;
                    q.emplace(i, j);
                }
            }
        }

        while (!q.empty()) {
            auto t = q.front();
            q.pop();

            int x = t.first, y = t.second;
            int s = score[x][y];

            for (int i = 0; i < 4; i++) {
                int newX = x + roww[i];
                int newY = y + coll[i];

                if (newX >= 0 && newX < n && newY >= 0 && newY < n && score[newX][newY] > 1 + s) {

                    score[newX][newY] = 1 + s;
                    q.emplace(newX, newY);
                }
            }
        }
    }

    /**
     * @brief This method calculates the maximum safeness factor for a given grid.
     * @param grid The grid for which the maximum safeness factor is calculated.
     * @return The maximum safeness factor for the given grid.
     */
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
        cout.tie(nullptr);
        int n = grid.size();
        if (grid[0][0] || grid[n - 1][n - 1]) {
            return 0;
        }

        vector<vector<int>> score(n, vector<int>(n, INT_MAX));
        bfs(grid, score, n);
        vector<vector<bool>> vis(n, vector<bool>(n, false));

        priority_queue<pair<int, pair<int, int>>> pq;
        pq.push({score[0][0], {0, 0}});

        while (!pq.empty()) {
            auto temp = pq.top().second;
            auto safe = pq.top().first;
            pq.pop();

            if (temp.first == n - 1 && temp.second == n - 1) {
                return safe;
            }
            vis[temp.first][temp.second] = true;

            for (int i = 0; i < 4; i++) {
                int newX = temp.first + roww[i];
                int newY = temp.second + coll[i];

                if (newX >= 0 && newX < n && newY >= 0 && newY < n && !vis[newX][newY]) {
                    int s = min(safe, score[newX][newY]);
                    pq.push({s, {newX, newY}});
                    vis[newX][newY] = true;
                }
            }
        }

        return -1;
    }
};
