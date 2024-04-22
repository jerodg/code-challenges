/// <summary>
/// Definition for a binary tree node.
/// </summary>
public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;

    /// <summary>
    /// Constructor for a binary tree node.
    /// </summary>
    /// <param name="val">The value of the node.</param>
    /// <param name="left">The left child of the node.</param>
    /// <param name="right">The right child of the node.</param>
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
    {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

/// <summary>
/// This class provides a solution for adding a row to a binary tree at a given depth.
/// </summary>
public class Solution
{
    /// <summary>
    /// This method adds a row to the binary tree at the given depth.
    /// </summary>
    /// <param name="root">The root of the binary tree.</param>
    /// <param name="val">The value to be added to the new row.</param>
    /// <param name="depth">The depth at which the new row should be added.</param>
    /// <returns>The root of the binary tree after adding the new row.</returns>
    public TreeNode AddOneRow(TreeNode root, int val, int depth)
    {
        if (depth == 1)
            return new TreeNode(val, root, null);

        AddOneRow(root, val, depth, 1);
        return root;
    }

    /// <summary>
    /// This method is a helper for AddOneRow. It recursively adds a row to the binary tree at the given depth.
    /// </summary>
    /// <param name="root">The root of the binary tree.</param>
    /// <param name="val">The value to be added to the new row.</param>
    /// <param name="depth">The depth at which the new row should be added.</param>
    /// <param name="currDepth">The current depth in the recursion.</param>
    private void AddOneRow(TreeNode root, int val, int depth, int currDepth)
    {
        if (currDepth + 1 == depth)
        {
            var left = root.left;
            var right = root.right;

            var newNodeLeft = new TreeNode(val, root.left, null);
            var newNodeRight = new TreeNode(val, null, root.right);

            root.left = newNodeLeft;
            root.right = newNodeRight;
        }
        else
        {
            if (root.left is not null)
                AddOneRow(root.left, val, depth, currDepth + 1);

            if (root.right is not null)
                AddOneRow(root.right, val, depth, currDepth + 1);
        }
    }
}
