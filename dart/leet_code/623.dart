/// Dart implementation of the LeetCode problem 623: Add One Row to Tree.
///
/// This module contains a class `Solution` with a method `addOneRow`.
/// The `addOneRow` method takes in three parameters:
/// - `root`: A TreeNode object representing the root of the tree.
/// - `val`: An integer representing the value to be added to the new row.
/// - `depth`: An integer representing the depth at which the new row should be added.
///
/// The method returns a TreeNode object representing the root of the tree after adding the new row.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `root` is a TreeNode object, `val` is an integer, and `depth` is a positive integer.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.

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
  /// Adds a new row to the tree at the specified depth.
  ///
  /// The method uses a stack to perform a depth-first search (DFS) on the tree from the root node.
  /// If the specified depth is reached, a new row is added to the tree.
  ///
  /// @param root The root of the tree.
  /// @param val The value to be added to the new row.
  /// @param depth The depth at which the new row should be added.
  /// @return A TreeNode object representing the root of the tree after adding the new row.
  TreeNode? addOneRow(TreeNode? root, int val, int depth) {
    // If the specified depth is 1, add a new root to the tree.
    if (depth == 1) return TreeNode(val, root, null);

    int cur = 1;
    List<TreeNode> stack = [root!];

    // Perform DFS on the tree until the specified depth is reached.
    while (stack.isNotEmpty && cur < depth - 1) {
      cur++;
      final len = stack.length;
      for (int i = 0; i < len; i++) {
        var temp = stack.removeAt(0);

        // If the current node has a left child, add it to the stack.
        if (temp.left != null) stack.add(temp.left!);

        // If the current node has a right child, add it to the stack.
        if (temp.right != null) stack.add(temp.right!);
      }
    }

    // Add a new row to the tree at the specified depth.
    final len = stack.length;
    for (int i = 0; i < len; i++) {
      var temp = stack.removeAt(0);
      var l = temp.left;
      var r = temp.right;
      temp.left = TreeNode(val, l, null);
      temp.right = TreeNode(val, null, r);
    }

    // Return the root of the tree after adding the new row.
    return root;
  }
}
