# frozen_string_literal: true

# Copyright © 2010-2024 JerodG <https://github.com/jerodg/> 2010-2024.
#
# This program is free software: you can redistribute it and/or modify it under the terms of the
# Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
# for more details.
#
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software. You should have received a copy of the SSPL along with this
# program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
#
# This file contains a solution for finding the shortest path in a grid with obstacles elimination.
# It defines a method `shortest_path`.

# Finds the shortest path in a grid with obstacles elimination.
# The grid is a 2D array where 0's represent free cells and 1's represent obstacles.
# You can eliminate at most k obstacles. If it is not possible to reach the target cell, return -1.
#
# @param [Array<Array<Integer>>] grid the grid
# @param [Integer] k the maximum number of obstacles that can be eliminated
# @return [Integer] the minimum number of steps to reach the target cell or -1 if it is not possible
def shortest_path(grid, k)
  m = grid.size
  n = grid[0].size
  visited = Array.new(m) { Array.new(n) { Array.new(k + 1, false) } }

  queue = [[0, 0, 0, 0]] # [row, col, steps, obstacles]

  until queue.empty?
    row, col, steps, obstacles = queue.shift

    # If we reach the target, return the number of steps
    return steps if row == m - 1 && col == n - 1

    # Check all possible moves (up, down, left, right)
    [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]].each do |new_row, new_col|
      next if new_row.negative? || new_row >= m || new_col.negative? || new_col >= n

      new_obstacles = obstacles + (grid[new_row][new_col] == 1 ? 1 : 0)

      # If the number of obstacles exceeds k, skip this move
      next if new_obstacles > k

      # If the state has been visited before, skip this move
      next if visited[new_row][new_col][new_obstacles]

      # Mark the state as visited
      visited[new_row][new_col][new_obstacles] = true

      # Add the new state to the queue
      queue << [new_row, new_col, steps + 1, new_obstacles]
    end
  end

  # If the target cannot be reached, return -1
  -1
end
