# Module: LeetCode
# The module encapsulates solutions for problems from LeetCode.
module LeetCode
  # Function: min_falling_path_sum
  # The function calculates the minimum falling path sum in a given grid.
  #
  # @param grid [Array<Array<Integer>>] The 2D array of integers representing the grid.
  #
  # @return [Integer] The minimum falling path sum in the grid.
  #
  # @example
  #   min_falling_path_sum([[1,2,3],[4,5,6],[7,8,9]]) #=> 12
  #
  # This function does not handle errors as it expects the input to always be a 2D array of integers.
  def min_falling_path_sum(grid)
    # Get the length of the grid
    n = grid.length
    # If the grid is 1x1, return the single value
    return grid[0][0] if n == 1
    # Initialize the dynamic programming array with the last row of the grid
    dp = grid[n - 1]

    # Iterate from the second last row to the first row
    (n - 2).downto(0) do |i|
      # Get the two smallest values in the dynamic programming array
      min1, min2 = dp.min(2)
      # Iterate over each column in the row
      dp.each_index do |j|
        # If the current value in the dynamic programming array is the smallest, add the second smallest value to the current grid value
        if dp[j] == min1
          dp[j] = grid[i][j] + min2
          # Otherwise, add the smallest value to the current grid value
        else
          dp[j] = grid[i][j] + min1
        end
      end
    end

    # Return the minimum value in the dynamic programming array
    dp.min
  end
end