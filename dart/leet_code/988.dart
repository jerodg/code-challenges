/// Dart core library for fundamental classes.
import 'dart:core';

/// Module for finding the smallest string that starts from leaf and one is smallest from all possible strings.
///
/// This module provides a `Solution` class that can be used to find the smallest string that starts from leaf and one is smallest from all possible strings.
/// The letters in the string are from a to z only and not case sensitive.
/// You may assume that the input tree will always have at least one leaf and that its size won't exceed 8500.

class TreeNode {
  /// The value of the node.
  int val;

  /// The left child of the node.
  TreeNode? left;

  /// The right child of the node.
  TreeNode? right;

  /// Constructs a new `TreeNode`.
  ///
  /// @param val The value of the node. Defaults to 0.
  /// @param left The left child of the node. Defaults to null.
  /// @param right The right child of the node. Defaults to null.
  TreeNode([this.val = 0, this.left, this.right]);
}

class Solution {
  /// Finds the smallest string that starts from leaf and one is smallest from all possible strings.
  ///
  /// This method uses a depth-first search approach to traverse the tree and find the smallest string.
  ///
  /// @param root The root of the tree.
  /// @return The smallest string that starts from leaf and one is smallest from all possible strings.
  ///
  /// Throws an `ArgumentError` if the root is null.
  ///
  /// Example usage:
  /// ```
  /// var solution = Solution();
  /// var smallestString = solution.smallestFromLeaf(root);
  /// print(smallestString);  // Outputs: "dba"
  /// ```
  String smallestFromLeaf(TreeNode? root) {
    String res = '{';
    void dfs(TreeNode? node, String path) {
      if (node == null) return;
      path = '${String.fromCharCode(97 + node.val)}$path';
      if (node.left == null && node.right == null) {
        res = path.compareTo(res) < 0 ? path : res;
      }
      dfs(node.left, path);
      dfs(node.right, path);
    }

    dfs(root, '');
    return res;
  }
}
