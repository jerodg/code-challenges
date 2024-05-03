# Module: LeetCode
# The module encapsulates solutions for problems from LeetCode.
module LeetCode
  # Function: wonderful_substrings
  # The function calculates the number of wonderful substrings in a given word. A wonderful string is a string where at most one letter appears an odd number of times.
  #
  # @param word [String] The word to find wonderful substrings in.
  #
  # @return [Integer] The number of wonderful substrings in the word.
  #
  # @example
  #   wonderful_substrings("aba") #=> 4
  #
  # This function does not handle errors as it expects the input to always be a string.
  def wonderful_substrings(word)
    # Initialize a hash to keep track of bitmasks
    btal = Hash.new(0)
    # Initialize the bitmask to 0
    btal[0] = 1
    # Initialize the bitmask
    bm = 0

    # Iterate over each character in the word
    word.chars.each do |ch|
      # Calculate the bitmask for the character
      b = 1 << (ch.ord - 'a'.ord)
      # If the bitmask for the character is not in the bitmask, add it
      if b & bm == 0
        bm += b
        # Otherwise, remove it
      else
        bm -= b
      end
      # Increment the count for the bitmask
      btal[bm] += 1
    end

    # Initialize the result to 0
    res = 0

    # Iterate over each bitmask in the hash
    btal.keys.each do |bm|
      # Add the number of substrings with the same bitmask to the result
      res += btal[bm] * (btal[bm] - 1)

      # Iterate over each bit in the bitmask
      (0..9).each do |b|
        # Calculate the shifted bitmask
        shift = 1 << b
        # Add the number of substrings with the shifted bitmask to the result
        res += btal[bm] * btal[bm ^ shift]
      end
    end
    # Return half of the result
    res / 2
  end
end