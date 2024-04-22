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

# Function to find the smallest string starting from leaf node
#
# This function finds the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
# The string consists of lowercase letters only.
# The path of a string is the concatenation of the characters in the nodes along the path from the leaf to the root.
#
# @param root [TreeNode] The root of the tree
# @return [String] The smallest string starting from leaf node
#
# @example
#   smallest_from_leaf(root) #=> "dba"
#
def smallest_from_leaf(root)
  result = []

  # Initialize a queue with the root node and an empty path
  queue = [[root, []]]
  until queue.empty?
    current, path = queue.shift
    # Prepend the current node's value to the path
    path = path.dup.unshift(current.val)

    # If the current node is a leaf node, update the result
    if current.left.nil? && current.right.nil?
      result = if result.empty?
                 path
               else
                 # Compare the current path with the result and keep the smaller one
                 [result, path].min
               end
    end

    # Add the left child to the queue if it exists
    queue.append([current.left, path]) if current.left
    # Add the right child to the queue if it exists
    queue.append([current.right, path]) if current.right
  end

  # Convert the result from integer values to characters and join them into a string
  result.map { |n| ('a'.ord + n).chr }.join
end