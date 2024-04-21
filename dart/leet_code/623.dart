/// Dart core library for fundamental classes.
import 'dart:core';

/// Module for adding a row of nodes at a given depth in a binary tree.
///
/// This module provides a `Solution` class that can be used to add a row of nodes at a given depth in a binary tree.
/// The original nodes at each depth d are moved to depth d+1.
/// The new nodes are inserted between the original nodes and their parents.
/// You may assume the tree's depth is at most d-1.

class TreeNode {
  /// The value of the node.
  int val;

  /// The left child of the node.
  TreeNode? left;

  /// The right child of the node.
  TreeNode? right;

  /// Constructs a new `TreeNode`.
  ///
  /// @param val The value of the node.
  /// @param left The left child of the node. Defaults to null.
  /// @param right The right child of the node. Defaults to null.
  TreeNode(this.val, {this.left, this.right});
}

class Solution {
  /// Adds a row of nodes at a given depth in a binary tree.
  ///
  /// This method uses a recursive approach to traverse the tree and add a row of nodes at the given depth.
  ///
  /// @param root The root of the tree.
  /// @param val The value of the new nodes.
  /// @param depth The depth at which to insert the new row of nodes.
  /// @return The root of the tree after adding the new row of nodes.
  ///
  /// Example usage:
  /// ```
  /// var solution = Solution();
  /// var newRoot = solution.addOneRow(root, 1, 2);
  /// ```
  TreeNode? addOneRow(TreeNode? root, int val, int depth) {
    // If root is null, return null
    if (root == null) return root;

    // If depth is 1, create a new TreeNode with root as left child
    if (depth == 1) return TreeNode(val, root);

    // If depth is 2, add new nodes as children of root
    if (depth == 2) {
      root.left = TreeNode(val, root.left, null);
      root.right = TreeNode(val, null, root.right);
    } else {
      // If depth is more than 2, recursively add a row of nodes at the given depth in the left and right subtrees
      addOneRow(root.left, val, depth - 1);
      addOneRow(root.right, val, depth - 1);
    }

    // Return the root of the tree
    return root;
  }
}
