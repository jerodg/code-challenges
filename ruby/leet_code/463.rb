# Function to calculate the perimeter of the islands in a grid
#
# This function calculates the perimeter of the islands in a 2D grid map of '1's (land) and '0's (water).
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# The perimeter is calculated by counting the edges of the land cells.
#
# @param grid [Array<Array<Integer>>] The 2D grid map of '1's (land) and '0's (water)
# @return [Integer] The total perimeter of the islands
#
# @example
#   island_perimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) #=> 16
#
def island_perimeter(grid)
  count = 0
  max_row_idx = grid.length - 1
  max_col_idx = grid.first.length - 1

  # Iterate over each cell in the grid
  (0..max_row_idx).each do |row|
    (0..max_col_idx).each do |col|
      # Skip if the cell is water
      next if grid[row][col] == 0

      # Start with 4 edges for a land cell
      edges = 4

      # If there is a land cell below the current cell, subtract 2 edges
      if row < max_row_idx
        edges -= 2 if grid[row + 1][col] == 1
      end

      # If there is a land cell to the right of the current cell, subtract 2 edges
      if col < max_col_idx
        edges -= 2 if grid[row][col + 1] == 1
      end

      # Add the remaining edges to the total count
      count += edges
    end
  end

  # Return the total count of edges, which is the perimeter of the islands
  count
end