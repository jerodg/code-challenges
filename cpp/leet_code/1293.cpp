// Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
//
// This program is free software: you can redistribute it and/or modify it under the terms of the
// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
// or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
// for more details.
//
// The above copyright notice and this permission notice shall be included in all copies or
// substantial portions of the Software. You should have received a copy of the SSPL along with this
// program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.

// Package 1293
// This file contains the implementation of a solution to find the shortest path in a grid with obstacles.
// The grid is represented as a 2D vector, and the number of obstacles that can be eliminated is given.
// The solution uses a breadth-first search algorithm to find the shortest path.

#include <array>
#include <climits>
#include <queue>
#include <vector>

// Class: Solution
// The Solution class encapsulates the method to find the shortest path in a grid with obstacles.
class Solution {
public:
    // Method: shortestPath
    // This method finds the shortest path in a grid with obstacles that can be eliminated.
    // It uses a breadth-first search algorithm to find the shortest path.
    //
    // Parameters:
    // grid - A 2D vector representing the grid. A 0 represents an open cell, and a 1 represents an obstacle.
    // k - The number of obstacles that can be eliminated.
    //
    // Returns:
    // The length of the shortest path. If no path exists, it returns -1.
    static int shortestPath(const std::vector<std::vector<int>>& grid, const int k) {
        // The number of rows in the grid
        const int m = grid.size();
        // The number of columns in the grid
        const int n = grid[0].size();
        // A 2D vector to keep track of visited cells
        std::vector<std::vector<int>> visited(m, std::vector<int>(n, 0));
        // A 2D vector to keep track of the number of obstacles encountered so far
        std::vector<std::vector<int>> obstacles(m, std::vector<int>(n, INT_MAX));
        // A queue to keep track of cells to be visited
        std::queue<std::tuple<int, int>> q;
        // An array to represent the four possible directions to move in the grid
         constexpr std::array<std::array<int, 2>, 4> d = {{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}};
        // The current number of steps taken
        int step = 0;
        // Add the starting cell to the queue
        q.emplace(0, 0);
        // Set the number of obstacles encountered at the starting cell to 0
        obstacles[0][0] = 0;
        // The number of cells at the current depth level
        int breadth = q.size();

        // Continue until all cells have been visited
        while(!q.empty()){
            // Get the coordinates of the current cell
            auto [x, y] = q.front();
            // If the current cell is the destination, return the number of steps taken
            if(x == m-1 && y == n-1)
                return step;
            // Try moving in all four directions
            for(auto &move : d){
                // Calculate the coordinates of the new cell
                int new_x = x + move[0];
                int new_y = y + move[1];
                // If the new cell is out of bounds, skip it
                if(new_x < 0 || new_x >= m || new_y < 0 || new_y >= n)
                    continue;
                // Calculate the number of obstacles encountered so far
                const int new_obs = obstacles[x][y] + grid[new_x][new_y];
                // If the new cell has more obstacles than the current cell, skip it
                if(new_obs >= obstacles[new_x][new_y])
                    continue;
                // If the number of obstacles encountered is less than or equal to k, add the new cell to the queue
                if(new_obs <= k) {
                    q.emplace(new_x, new_y);
                    obstacles[new_x][new_y] = new_obs;
                }
            }
            // Mark the current cell as visited
            visited[x][y] = 1;
            // Remove the current cell from the queue
            q.pop();
            // Decrease the number of cells at the current depth level
            breadth--;
            // If all cells at the current depth level have been visited, move to the next depth level
            if(breadth == 0){
                step++;
                breadth = q.size();
            }
        }
        // If no path exists, return -1
        return -1;
    }
};
