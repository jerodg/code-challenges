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
# You should have received a copy of the SSPL along with this program.
# If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

# The ListNode class represents a node in a singly linked list.
# Each node holds a value and a reference to the next node in the list.
class ListNode
  # The value of the node.
  attr_accessor :val
  # The next node in the list.
  attr_accessor :next

  # Initializes a new instance of the ListNode class.
  #
  # @param val [Integer] The value of the node.
  # @param _next [ListNode] The next node in the list.
  def initialize(val = 0, _next = nil)
    @val = val
    @next = _next
  end
end

# The double_it method takes a linked list of digits and returns an array of digits
# representing the number formed by the linked list, doubled.
#
# @param head [ListNode] The head of the linked list.
# @return [Array<Integer>] An array of digits representing the doubled number.
def double_it(head)
  nums = []
  node = head
  while node
    nums << node.val
    node = node.next
  end

  nums = nums.join.to_i * 2
  nums.to_s.chars.map(&:to_i)
end
