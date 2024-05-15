# Copyright © 2010-2024 JerodG <https://github.com/jerodg/> 2010-2024.
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

# frozen_string_literal: true

# This file contains a method `maximum_happiness_sum` which calculates the maximum happiness sum
# given an array of happiness values and a number `k`. The method sorts the happiness array in
# ascending order, then iteratively pops the highest happiness value, subtracts the current
# iteration index from it, and adds it to the total sum.
# The iteration stops if the calculated happiness value becomes negative.

# @param [Array<Integer>] happiness An array of integers representing happiness values.
# @param [Integer] k The number of times to subtract the iteration index from the highest happiness value.
# @return [Integer] The maximum happiness sum.
def maximum_happiness_sum(happiness, k)
  # Sort the happiness array in ascending order
  happiness.sort!

  # Initialize the total sum to 0
  total = 0

  # Iterate `k` times
  k.times do |i|
    # Pop the highest happiness value
    h = happiness.pop

    # Subtract the current iteration index from the popped happiness value
    l = h - i

    # Break the loop if the calculated happiness value is negative
    break if l.negative?

    # Add the calculated happiness value to the total sum
    total += l
  end

  # Return the total sum
  total
end
