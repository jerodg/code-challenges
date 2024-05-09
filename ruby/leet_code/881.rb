# frozen_string_literal: true

# Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the Server Side Public License (SSPL) as
# published by MongoDB, Inc., either version 1 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# SSPL for more details.
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# You should have received a copy of the SSPL along with this program.
# If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
#
# This file contains the implementation of the `num_rescue_boats` function
# which calculates the minimum number of boats required to rescue all people
# given their weights and the weight limit of each boat. It also includes
# a helper function `sorted?` to check if an array is sorted.

# Checks if an array is sorted in ascending order.
#
# @param array [Array<Number>] the array to check
# @return [Boolean] true if the array is sorted, false otherwise
def sorted?(array)
  array.each_cons(2).all? { |a, b| a <= b }
end

# Calculates the minimum number of boats required to rescue all people.
#
# The function sorts the array of people's weights, then uses a two-pointer
# technique to iterate from both ends of the array towards the middle.
# This approach ensures that the minimum number of boats is used, as it
# always tries to pair the lightest person with the heaviest person.
#
# @param people [Array<Number>] the weights of the people to rescue
# @param limit [Number] the weight limit of each boat
# @return [Number] the minimum number of boats required
def num_rescue_boats(people, limit)
  people.sort! unless sorted?(people)
  i = 0
  j = people.length - 1
  boats = 0

  while i <= j
    i += 1 if people[i] + people[j] <= limit
    j -= 1
    boats += 1
  end
  boats
end
