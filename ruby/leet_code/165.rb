# Module: LeetCode
# The module encapsulates solutions for problems from LeetCode.
module LeetCode
  # Function: compare_version
  # The function compares two version numbers (version1 and version2).
  #
  # @param version1 [String] The first version number to compare.
  # @param version2 [String] The second version number to compare.
  #
  # @return [Integer] Returns 1 if version1 > version2, -1 if version1 < version2, otherwise 0.
  #
  # @example
  #   compare_version("1.0.1", "1") #=> 1
  #
  # This function does not handle errors as it expects the input to always be a string.
  def compare_version(version1, version2)
    # Calculate the numeric value of version1
    v1 = calculate_version(version1)
    # Calculate the numeric value of version2
    v2 = calculate_version(version2)

    # Compare the two versions and return the result
    if v1 > v2
      1
    elsif v2 > v1
      -1
    else
      0
    end
  end

  # Function: calculate_version
  # The function calculates the numeric value of a version number.
  #
  # @param str [String] The version number to calculate.
  #
  # @return [Float] The numeric value of the version number.
  #
  # @example
  #   calculate_version("1.0.1") #=> 1.01
  #
  # This function does not handle errors as it expects the input to always be a string.
  def calculate_version(str)
    # Initialize the delimiter to 1
    del = 1

    # Split the version number by '.' and calculate the numeric value
    str.split('.').map do |v|
      # Multiply the version part by the delimiter and store the result
      r = v.to_i * del
      # Divide the delimiter by 10 for the next iteration
      del = del / 10.0
      # Return the result
      r
    end.sum
  end
end