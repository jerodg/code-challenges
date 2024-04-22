# Module LeetCode
#
# This module contains the solution for the LeetCode problem 200, "Number of Islands".
# The problem is about counting the number of islands in a 2D grid map of '1's (land) and '0's (water).
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
module LeetCode
  # Constants representing the land, water and visited land
  LAND = "1".freeze
  WATER = "0".freeze
  VISITED = "X".freeze

  # Function to count the number of islands in a grid
  #
  # @param grid [Array<Array<String>>] The 2D grid map of '1's (land) and '0's (water)
  # @return [Integer] The number of islands
  #
  # @example
  #   num_islands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]) #=> 1
  #
  def num_islands(grid)
    count = 0
    (0...grid.length).each do |r|
      (0...grid.first.length).each do |c|
        if grid[r][c] == LAND
          count += 1
          fill(grid, r, c)
        end
      end
    end
    count
  end

  # Function to mark the visited land in a grid
  #
  # @param grid [Array<Array<String>>] The 2D grid map of '1's (land) and '0's (water)
  # @param start_r [Integer] The starting row index
  # @param start_c [Integer] The starting column index
  #
  # @example
  #   fill([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 0, 0)
  #
  def fill(grid, start_r, start_c)
    cols = grid.first.length
    todo = [start_r * cols + start_c]
    until todo.empty?
      i = todo.shift
      r = i / cols
      c = i % cols
      next if grid[r][c] == VISITED
      grid[r][c] = VISITED
      todo << i - cols if r > 0 && grid[r - 1][c] == LAND
      todo << i + cols if r < grid.length - 1 && grid[r + 1][c] == LAND
      todo << i - 1 if c > 0 && grid[r][c - 1] == LAND
      todo << i + 1 if c < cols - 1 && grid[r][c + 1] == LAND
    end
  end
end