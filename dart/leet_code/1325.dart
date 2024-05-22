/**
 * Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see SSPL.
 */

/// Package leet_code
///
/// This file contains the implementation of a binary tree node and a solution
/// for removing leaf nodes with a specific value.
library;

/// A class representing a node in a binary tree.
///
/// Each node has an integer value and two child nodes: left and right.
/// The child nodes are also instances of the TreeNode class.
class TreeNode {
  /// The value of the node.
  int val;

  /// The left child of the node.
  TreeNode? left;

  /// The right child of the node.
  TreeNode? right;

  /// Creates a new TreeNode with the given value and child nodes.
  ///
  /// The value defaults to 0 if not provided.
  /// The child nodes default to null if not provided.
  TreeNode([this.val = 0, this.left, this.right]);
}

/// A class providing a solution for removing leaf nodes with a specific value.
class Solution {
  /// Removes all leaf nodes with the given target value from the tree rooted at the given node.
  ///
  /// This method works by recursively removing leaf nodes from the left and right subtrees,
  /// and then checking if the current node has become a leaf node with the target value.
  ///
  /// @param root The root of the tree from which to remove nodes.
  /// @param target The value of the leaf nodes to remove.
  /// @return The root of the tree after removing nodes, or null if the root was removed.
  TreeNode? removeLeafNodes(TreeNode? root, int target) {
    if (root == null) {
      return null;
    }
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);
    if (root.left == null && root.right == null && root.val == target) {
      return null;
    }
    return root;
  }
}
