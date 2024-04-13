# Module: LeetCode
# This module contains solutions for problems from LeetCode.
module LeetCode
  # Function: maximal_rectangle
  # This function calculates the maximal rectangle in a matrix.
  #
  # @param matrix [Array<Array<String>>] The input matrix.
  # @return [Integer] The area of the maximal rectangle.
  def maximal_rectangle(matrix)
    return 0 if matrix.empty?

    m, n = matrix.size, matrix[0].size
    left, right, height = Array.new(n, 0), Array.new(n, n), Array.new(n, 0)
    max_area = 0

    (0...m).each do |i|
      cur_left, cur_right = 0, n

      (0...n).each do |j|
        if matrix[i][j] == '1'
          height[j] += 1
          left[j] = [left[j], cur_left].max
        else
          height[j] = 0
          left[j] = 0
          cur_left = j + 1
        end
      end

      (n - 1).downto(0) do |j|
        if matrix[i][j] == '1'
          right[j] = [right[j], cur_right].min
        else
          right[j] = n
          cur_right = j
        end
      end

      max_area = [max_area, *(0...n).map { |j| (right[j] - left[j]) * height[j] }].max
    end

    max_area
  end
end
