# frozen_string_literal: true

# Module: LeetCode
# The module encapsulates the solution for the problem from LeetCode.
# This specific problem is about finding the longest ideal string.
module LeetCode
  # Function: longest_ideal_string
  # The function calculates the longest ideal string.
  #
  # Parameters:
  # s - A string input for which the longest ideal string is to be calculated. It is expected to be a string.
  # k - A number that represents the maximum allowed difference in ASCII values between any two characters in the ideal string. It is expected to be an integer.
  #
  # Returns:
  # The function returns the length of the longest ideal string that can be formed from the input string 's' by changing at most 'k' ASCII values of any character. The return type is an integer.
  #
  # Error Handling:
  # The function does not explicitly handle errors. It assumes that the inputs are of the correct type and within the expected range.
  # @param [Object] s
  # @param [Object] k
  def longest_ideal_string(s, k)
    # An array to store the ASCII values of the characters in the string 's'.
    ascii = Array.new(123, 0)

    # Iterating over each character in the string 's'.
    s.each_char do |ch|
      # Getting the ASCII value of the character.
      i = ch.ord

      # Calculating the start and end indices for the range of ASCII values that can be formed by changing the ASCII value of the character by at most 'k'.
      start_index = [0, i - k].max
      end_index = [122, i + k].min

      # Updating the ASCII value of the character in the 'ascii' array to be the maximum ASCII value that can be formed by changing the ASCII value of the character by at most 'k'.
      ascii[i] = (start_index..end_index).map { |j| ascii[j] }.max + 1
    end

    # Returning the maximum ASCII value in the 'ascii' array, which represents the length of the longest ideal string that can be formed from the string 's'.
    ascii.max
  end
end
