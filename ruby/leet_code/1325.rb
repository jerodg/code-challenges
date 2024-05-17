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
# This file contains a solution for removing leaf nodes from a binary tree that have a specific target value.
# It defines a TreeNode class and a method `remove_leaf_nodes`.

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

# Removes all the leaf nodes from the binary tree that have the target value.
#
# @param [TreeNode] root the root of the binary tree
# @param [Integer] target the target value to remove
# @return [TreeNode, nil] the root of the modified tree, or nil if the tree is empty or all nodes were removed
def remove_leaf_nodes(root, target)
  return unless root

  # Recursively remove leaf nodes from the left and right subtrees
  root.left = remove_leaf_nodes(root.left, target)
  root.right = remove_leaf_nodes(root.right, target)

  # If the current node is a leaf node and its value is the target, remove it
  # Otherwise, return the node
  root if root.left || root.right || root.val != target
end
