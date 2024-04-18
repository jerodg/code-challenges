using System;

/// <summary>
/// Definition for a binary tree node.
/// </summary>
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    /// <summary>
    /// Initializes a new instance of the TreeNode class.
    /// </summary>
    /// <param name="val">The value of the node.</param>
    /// <param name="left">The left child of the node.</param>
    /// <param name="right">The right child of the node.</param>
    public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/// <summary>
/// Provides a solution for finding the smallest string starting from leaf of a binary tree.
/// </summary>
public class Solution {
    /// <summary>
    /// Finds the smallest string starting from leaf of a binary tree.
    /// </summary>
    /// <param name="root">The root of the binary tree.</param>
    /// <returns>The smallest string starting from leaf of the binary tree.</returns>
    public string SmallestFromLeaf(TreeNode root) {
        if (root == null) {
            return "";
        }
        return Helper(root, "");
    }

    /// <summary>
    /// Helper function to recursively find the smallest string starting from leaf of a binary tree.
    /// </summary>
    /// <param name="root">The current node in the binary tree.</param>
    /// <param name="str">The current string formed from the path in the binary tree.</param>
    /// <returns>The smallest string starting from leaf of the binary tree.</returns>
    private string Helper(TreeNode root, string str) {
        if (root == null) {
            return "";
        }

        // Convert the value of the node to a character and prepend it to the current string
        str = (char)('a' + root.val) + str;

        // If the node is a leaf node, return the current string
        if (root.left == null && root.right == null) {
            return str;
        }

        // If the node has no left child, continue with the right child
        if (root.left == null) {
            return Helper(root.right, str);
        }

        // If the node has no right child, continue with the left child
        if (root.right == null) {
            return Helper(root.left, str);
        }

        // If the node has both children, continue with the child that forms the smaller string
        string left = Helper(root.left, str);
        string right = Helper(root.right, str);
        return left.CompareTo(right) < 0 ? left : right;
    }
}
