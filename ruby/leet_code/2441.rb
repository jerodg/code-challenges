# Module: LeetCode
# The module encapsulates solutions for problems from LeetCode.
module LeetCode
  # Function: find_max_k
  # The function finds the maximum positive integer in the array that also has its negative in the array.
  #
  # @param nums [Array<Integer>] The array of integers to search through.
  #
  # @return [Integer] The maximum positive integer that also has its negative in the array, or -1 if no such integer exists.
  #
  # @example
  #   find_max_k([3, -1, 1, -3, 2]) #=> 3
  #
  # This function does not handle errors as it expects the input to always be an array of integers.
  def find_max_k(nums)
    # Initialize the maximum positive integer to -1
    max_positive = -1
    # Initialize an empty hash to keep track of visited numbers
    visited = {}

    # Iterate over each number in the array
    nums.each do |num|
      # If the number is positive, its negative has been visited, and it's greater than the current maximum positive
      if num > 0 && visited.key?(-num) && num > max_positive
        # Update the maximum positive
        max_positive = num
        # If the number is negative, its positive has been visited, and its absolute value is greater than the current maximum positive
      elsif num < 0 && visited.key?(-num) && -num > max_positive
        # Update the maximum positive
        max_positive = -num
      end
      # Mark the number as visited
      visited[num] = true
    end

    # Return the maximum positive integer
    max_positive
  end
end
