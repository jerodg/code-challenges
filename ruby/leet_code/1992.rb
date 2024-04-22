# Function to find all farmland in a 2D binary grid
#
# This function finds all farmland in a 2D binary grid, where '1' represents a plot of farmland and '0' represents a plot of non-farmland.
# Each farmland is represented as a rectangle with no other farmland in any adjacent plots.
# The farmland rectangles are represented as an array of their top-left and bottom-right coordinates.
#
# @param land [Array<Array<Integer>>] The 2D binary grid of farmland and non-farmland
# @return [Array<Array<Integer>>] An array of farmland rectangles, where each rectangle is represented as an array of its top-left and bottom-right coordinates
#
# @example
#   find_farmland([[1,0,0],[0,1,1],[0,1,1]]) #=> [[0,0,0,0],[1,1,2,2]]
#
def find_farmland(land)
  result = []
  memo = {}

  land.each_with_index do |row_values, row|
    col = 0

    while col < row_values.size
      # If the current column is in the memo, update the farmland rectangle or remove it from the memo
      if memo.include?(col)
        last_col = memo[col][3]

        if row_values[col].zero?
          # If the current plot is non-farmland, add the farmland rectangle to the result and remove it from the memo
          result << memo.delete(col)
        else
          # If the current plot is farmland, update the bottom-right coordinate of the farmland rectangle
          memo[col][2] += 1
        end

        col = last_col + 1
        # If the current plot is farmland and the current column is not in the memo, add a new farmland rectangle to the memo
      elsif row_values[col] == 1
        first_col = col

        # Find the rightmost plot of the farmland
        true while row_values[col += 1] == 1
        # Add the farmland rectangle to the memo
        memo[first_col] = [row, first_col, row, col - 1]
      else
        col += 1
      end
    end
  end

  # Add the remaining farmland rectangles in the memo to the result
  result.concat(memo.values)
end