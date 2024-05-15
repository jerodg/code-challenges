# frozen_string_literal: true

# Copyright ©2010-2024 JerodG <https://github.com/jerodg/>
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

# This file contains a method to find the maximum amount of gold that can be collected in a grid.
# The grid is a 2D array where each cell represents a gold mine with a certain amount of gold.
# The method uses a depth-first search (DFS) algorithm to explore all possible paths in the grid,
# starting from each cell that contains gold. The DFS algorithm is implemented using a lambda function
# for recursion. The algorithm keeps track of the maximum amount of gold collected so far and updates
# it whenever a path with more gold is found.

def get_maximum_gold(grid)
  # The number of rows in the grid
  m = grid.length
  # The number of columns in the grid
  n = grid[0].length
  # The maximum amount of gold collected so far
  max_gold = 0

  # The DFS algorithm implemented as a lambda function
  dfs_backtrack = lambda do |i, j, current_gold|
    # Return if the current cell is out of bounds or does not contain gold
    return if i.negative? || i >= m || j.negative? || j >= n || (grid[i][j]).zero?

    # The amount of gold in the current cell
    gold_in_current_cell = grid[i][j]
    # Add the gold in the current cell to the total amount of gold collected so far
    current_gold += gold_in_current_cell
    # Update the maximum amount of gold if the current total is greater
    max_gold = [max_gold, current_gold].max
    # Temporarily remove the gold from the current cell to avoid visiting it again
    temp = grid[i][j]
    grid[i][j] = 0
    # Recursively explore the neighboring cells
    dfs_backtrack.call(i + 1, j, current_gold)
    dfs_backtrack.call(i - 1, j, current_gold)
    dfs_backtrack.call(i, j + 1, current_gold)
    dfs_backtrack.call(i, j - 1, current_gold)
    # Put the gold back into the current cell
    grid[i][j] = temp
  end

  # Iterate over each cell in the grid
  (0...m).each do |i|
    (0...n).each do |j|
      # If the current cell contains gold, start the DFS algorithm from this cell
      dfs_backtrack.call(i, j, 0) if grid[i][j] != 0
    end
  end
  # Return the maximum amount of gold collected
  max_gold
end
