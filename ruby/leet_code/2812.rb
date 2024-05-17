# frozen_string_literal: true

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
#
# This file contains a solution for calculating the maximum safeness factor of a grid.
# It defines a DisjointSet class and a method `maximum_safeness_factor`.

# DisjointSet class represents a disjoint-set data structure.
# It provides operations for union, find and size.
class DisjointSet
  # Initializes a new instance of the DisjointSet class.
  #
  # @param [Integer] n the number of elements in the set
  def initialize(n)
    @parent = Array.new(n) { -1 }
  end

  # Finds the representative of the set that a belongs to.
  #
  # @param [Integer] a an element of the set
  # @return [Integer] the representative of the set
  def find(a)
    return a if (@parent[a]).negative?

    @parent[a] = find(@parent[a])
  end

  # Unions the sets that a and b belong to.
  #
  # @param [Integer] a an element of the set
  # @param [Integer] b an element of the set
  # @return [Integer] the representative of the unioned set
  def union(a, b)
    x = find(a)
    y = find(b)
    return x if x == y

    if size(x) < size(y)
      t = x
      x = y
      y = t
    end
    @parent[x] += @parent[y]
    @parent[y] = x
    x
  end

  # Returns the size of the set that a belongs to.
  #
  # @param [Integer] a an element of the set
  # @return [Integer] the size of the set
  def size(a)
    -@parent[find(a)]
  end
end

# Calculates the maximum safeness factor of a grid.
# The safeness factor is defined as the minimum distance to a cell with value 0.
#
# @param [Array<Array<Integer>>] grid the grid
# @return [Integer] the maximum safeness factor
def maximum_safeness_factor(grid)
  n = grid.size
  q = []
  distance = Array.new(n * n) do
    next if (grid[_1 / n][_1 % n]).zero?

    q << _1
    0
  end
  until q.empty?
    r, c = q.shift.divmod(n)
    if c < n - 1 && distance[r * n + c + 1].nil?
      distance[r * n + c + 1] = distance[r * n + c] + 1
      q << r * n + c + 1
    end
    if c.positive? && distance[r * n + c - 1].nil?
      distance[r * n + c - 1] = distance[r * n + c] + 1
      q << r * n + c - 1
    end
    if r < n - 1 && distance[(r + 1) * n + c].nil?
      distance[(r + 1) * n + c] = distance[r * n + c] + 1
      q << (r + 1) * n + c
    end
    if r.positive? && distance[(r - 1) * n + c].nil?
      distance[(r - 1) * n + c] = distance[r * n + c] + 1
      q << (r - 1) * n + c
    end
  end

  ds = DisjointSet.new(n * n)
  (0...n * n).sort_by { -distance[_1] }.each do
    ds.union(_1, 1 + _1) if _1 % n < n - 1 && distance[_1] <= distance[_1 + 1]
    ds.union(_1, _1 - 1) if (_1 % n).positive? && distance[_1] <= distance[_1 - 1]
    ds.union(_1, _1 + n) if _1 / n < n - 1 && distance[_1] <= distance[_1 + n]
    ds.union(_1, _1 - n) if (_1 / n).positive? && distance[_1] <= distance[_1 - n]
    return distance[_1] if ds.find(0) == ds.find(n * n - 1)
  end
end
