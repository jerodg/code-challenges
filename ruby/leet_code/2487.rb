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
# This file contains the implementation of the `ListNode` class and the `remove_nodes` function.
# The `ListNode` class is used to create nodes for a linked list, where each node contains a value and a reference to the next node.
# The `remove_nodes` function is used to remove nodes from a linked list that have a smaller value than the next node.

# Class representing a node in a linked list.
# Each node contains a value and a reference to the next node.
class ListNode
  attr_accessor :val, :next

  # Initializes a new instance of the ListNode class.
  #
  # @param val [Number] the value of the node
  # @param _next [ListNode, nil] the next node in the linked list
  def initialize(val = 0, _next = nil)
    @val = val
    @next = _next
  end
end

# Removes nodes from a linked list that have a smaller value than the next node.
#
# The function uses a recursive approach to traverse the linked list from the end to the start.
# If the value of the current node is smaller than the value of the next node, the current node is removed.
#
# @param head [ListNode] the head of the linked list
# @return [ListNode] the head of the linked list after removing nodes
def remove_nodes(head)
  return head if head.next.nil?

  head.next = remove_nodes(head.next) unless head.next.nil?
  return head.next if head.next.val > head.val

  head
end
