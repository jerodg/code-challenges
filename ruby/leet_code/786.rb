# frozen_string_literal: true

# This file contains a method to find the Kth smallest prime fraction from an array of integers.
# The method uses a binary search approach to find the fraction.
# Copyright ©2010-2024 JerodG <https://github.com/jerodg/>
# This program is free software: you can redistribute it and/or modify it under the terms of the
# Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
# or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
# for more details.
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software. You should have received a copy of the SSPL along with this
# program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

# Finds the Kth smallest prime fraction from an array of integers.
#
# @param arr [Array<Integer>] the array of integers
# @param k [Integer] the Kth smallest fraction to find
# @return [Array<Integer>] the Kth smallest prime fraction
def kth_smallest_prime_fraction(arr, k)
  # Length of the array
  n = arr.length
  # Initialize the answer as [0, 1]
  ans = [0, 1]
  # Initialize the left and right boundaries for the binary search
  l = 0.0
  r = 1.0

  # Start the loop for the binary search
  loop do
    # Calculate the middle point
    m = (l + r) / 2
    # Reset the numerator of the answer
    ans[0] = 0
    # Initialize the count of fractions that are less than or equal to m
    count = 0
    # Initialize the index for the denominator
    j = 1

    # Iterate over the array
    (0...n).each do |i|
      # Find the smallest j such that arr[i] <= m * arr[j]
      j += 1 while j < n && arr[i] > m * arr[j]
      # Update the count
      count += n - j
      # If j has reached the end of the array, break the loop
      break if j == n

      # If the current fraction is larger than the current answer, update the answer
      if ans[0] * arr[j] < ans[1] * arr[i]
        ans[0] = arr[i]
        ans[1] = arr[j]
      end
    end

    # If the count is equal to k, return the answer
    return ans if count == k

    # If the count is less than k, update the left boundary; otherwise, update the right boundary
    if count < k
      l = m
    else
      r = m
    end
  end
end
