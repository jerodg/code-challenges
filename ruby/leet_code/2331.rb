# frozen_string_literal: true

# Copyright © 2010-2024 https://github.com/jerodg/
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
# program. If not, see https://www.mongodb.com/licensing/server-side-public-license
#
# This file contains a solution for checking if a string is a valid sequence from root to leaves path in a binary tree.
# It defines a TreeNode class and a method `evaluate_tree`.

# TreeNode class represents a node in a binary tree.
# Each node contains a value and pointers to its left and right child nodes.
class TreeNode
  # @attr_accessor [Integer] val the value of the node
  # @attr_accessor [TreeNode] left the left child of the node
  # @attr_accessor [TreeNode] right the right child of the node
  attr_accessor :val, :left, :right

  # Initializes a new instance of the TreeNode class.
  #
  # @param [Integer] val the value of the node
  # @param [TreeNode] left the left child of the node
  # @param [TreeNode] right the right child of the node
  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# Evaluates the binary tree based on the value of each node.
# If the value is 1, it returns true.
# If the value is 0, it returns false.
# If the value is 2, it evaluates the right or left child node.
# For any other value, it evaluates both the right and left child nodes.
#
# @param [TreeNode] root the root of the binary tree
# @return [Boolean] the result of the evaluation
def evaluate_tree(root)
  # If the value of the root node is 1, return true
  case root.val
  when 1
    true
    # If the value of the root node is 0, return false
  when 0
    false
    # If the value of the root node is 2, evaluate the right or left child node
  when 2
    evaluate_tree(root.right) || evaluate_tree(root.left)
    # For any other value, evaluate both the right and left child nodes
  else
    evaluate_tree(root.right) && evaluate_tree(root.left)
  end
end
