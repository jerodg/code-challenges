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

# This file contains a method to calculate the maximum score after flipping and rearranging a binary matrix.
# The matrix is a 2D array where each cell contains a binary digit (0 or 1).
# The method uses a greedy algorithm to first flip rows and then columns to maximize the score.
# The score is calculated as the sum of binary numbers represented by each row in the matrix.

# @param grid [Array<Array<Integer>>] The binary matrix
# @return [Integer] The maximum score after flipping and rearranging the matrix
def matrix_score(grid)
  # Initialize the result to 0
  result = 0
  # Get the number of rows and columns in the grid
  m = grid.length
  n = grid[0].length

  # Iterate over each row in the grid
  (0...m).each do |i|
    # Determine if the row needs to be flipped
    flip = grid[i][0].zero?
    # Initialize the current row's score to 0
    curr = 0
    # Iterate over each cell in the row
    (0...n).each do |j|
      # If the row needs to be flipped, flip the cell
      if flip
        grid[i][j] = grid[i][j] == 1 ? 0 : 1
      end
      # Calculate the current row's score
      curr = curr * 2 + grid[i][j]
    end
    # Add the current row's score to the result
    result += curr
  end

  # Iterate over each column in the grid, starting from the second column
  (1...n).each do |i|
    # Count the number of 0s in the column
    count = grid.map { |row| row[i] == 1 ? 0 : 1 }.sum
    # If the number of 0s is more than half of the number of rows, flip the column
    if count > m / 2
      # Add the score gained from flipping the column to the result
      result += (2 ** (n - i - 1)) * (count - m + count)
    end
  end
  # Return the result
  result
end
