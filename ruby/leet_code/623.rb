# Class TreeNode
#
# This class represents a node in a binary tree. Each node has a value, and references to its left and right children.
#
class TreeNode
  attr_accessor :val, :left, :right

  # Initialize a new instance of the TreeNode class
  #
  # @param val [Integer] The value of the node
  # @param left [TreeNode, nil] The left child of the node
  # @param right [TreeNode, nil] The right child of the node
  #
  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# Function to add a row of nodes with a given value at a given depth in the tree
#
# @param root [TreeNode] The root of the tree
# @param val [Integer] The value for the new row of nodes
# @param depth [Integer] The depth at which to add the new row
# @return [TreeNode] The root of the modified tree
#
# @example
#   add_one_row(root, 1, 2) #=> root with an added row of nodes with value 1 at depth 2
#
def add_one_row(root, val, depth)
  if depth == 1
    new_root = TreeNode.new(val)
    new_root.left = root
    return new_root
  end

  dfs_insert(root, val, depth, 1)
  root
end

# Function to insert a new row of nodes at a given depth in the tree using depth-first search
#
# @param node [TreeNode] The current node
# @param val [Integer] The value for the new row of nodes
# @param target_depth [Integer] The depth at which to add the new row
# @param current_depth [Integer] The current depth in the tree
#
# @example
#   dfs_insert(root, 1, 2, 1) #=> root with an added row of nodes with value 1 at depth 2
#
def dfs_insert(node, val, target_depth, current_depth)
  return unless node
  return if current_depth == target_depth

  if current_depth == target_depth - 1
    old_left = node.left
    old_right = node.right

    node.left = TreeNode.new(val)
    node.right = TreeNode.new(val)

    node.left.left = old_left
    node.right.right = old_right
  else
    dfs_insert(node.left, val, target_depth, current_depth + 1)
    dfs_insert(node.right, val, target_depth, current_depth + 1)
  end
end