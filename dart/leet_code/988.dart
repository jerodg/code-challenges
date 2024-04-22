/// Dart core library for fundamental classes.
import 'dart:core';

/// Dart implementation of the LeetCode problem 988: Smallest String Starting From Leaf.
///
/// This module contains a class `Solution` with a method `smallestFromLeaf`.
/// The `smallestFromLeaf` method takes in one parameter:
/// - `root`: A TreeNode object representing the root of the tree.
///
/// The method returns a string representing the smallest string that starts from leaf and one is smallest from all possible strings.
/// The letters in the string are from a to z only and not case sensitive.
/// You may assume that the input tree will always have at least one leaf and that its size won't exceed 8500.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `root` is a TreeNode object.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.
/// - Throws an `ArgumentError` if the root is null.

class TreeNode {
  int val;
  TreeNode? left;
  TreeNode? right;

  /// Constructor for the TreeNode class.
  ///
  /// @param val The value of the node.
  /// @param left The left child of the node.
  /// @param right The right child of the node.
  TreeNode([this.val = 0, this.left, this.right]);
}

class Solution {
  /// Finds the smallest string that starts from leaf and one is smallest from all possible strings.
  ///
  /// This method uses a depth-first search approach to traverse the tree and find the smallest string.
  /// It iterates over each node in the tree. If the node is a leaf node, it compares the current path with the smallest path found so far and updates it if necessary.
  /// It uses a string to keep track of the current path and appends the character corresponding to the current node's value to the beginning of the string.
  ///
  /// @param root The root of the tree.
  /// @return The smallest string that starts from leaf and one is smallest from all possible strings.
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
