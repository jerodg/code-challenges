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
/// This file contains the implementation of a solution for a LeetCode problem.
/// The problem involves distributing coins in a binary tree.
/// A class representing a node in a binary tree.
///
/// Each node contains an integer value and may have a left and/or right child.
class TreeNode {
  /// The value of the node.
  int val;

  /// The left child of the node.
  TreeNode? left;

  /// The right child of the node.
  TreeNode? right;

  /// Creates a new TreeNode with the given value and children.
  ///
  /// @param val The value of the node. Defaults to 0 if not provided.
  /// @param left The left child of the node. Defaults to null if not provided.
  /// @param right The right child of the node. Defaults to null if not provided.
  TreeNode([this.val = 0, this.left, this.right]);
}

/// A class representing the solution to the problem.
///
/// The solution involves calculating the number of moves required to distribute
/// the coins in the binary tree such that each node has exactly one coin.
class Solution {
  /// The total number of moves required to distribute the coins.
  int? _moves;

  /// Calculates the number of moves required to distribute the coins in the subtree rooted at the given node.
  ///
  /// @param node The root of the subtree.
  /// @return The number of coins that need to be moved to or from the parent of the node.
  int calculateMoves(TreeNode? node) {
    if (node == null) return 0;

    int leftMoves = calculateMoves(node.left);
    int rightMoves = calculateMoves(node.right);

    _moves = _moves! + leftMoves.abs() + rightMoves.abs();

    return node.val - 1 + leftMoves + rightMoves;
  }

  /// Distributes the coins in the binary tree rooted at the given node.
  ///
  /// @param root The root of the binary tree.
  /// @return The total number of moves required to distribute the coins.
  int distributeCoins(TreeNode? root) {
    _moves = 0;
    calculateMoves(root);
    return _moves!;
  }
}
