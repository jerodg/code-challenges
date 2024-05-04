import javax.swing.tree.TreeNode;

/**
 * This class provides a solution for adding a row of nodes with a given value at a specified depth in a binary tree.
 * The root node is at depth 1, and its children are at depth 2, and so on.
 * If the depth is 1, a new root node is created with the given value, and the original root node becomes the left child of the new root.
 * If the depth is not 1, then for each node on the current level, create a new node with the given value as the left child of the original node, and the original left child becomes the left child of the new node. Do the same for the right child.
 */
class Solution {

    /**
     * Adds a row of nodes with a given value at a specified depth in the binary tree.
     *
     * @param root  The root node of the binary tree.
     * @param val   The value for the new row of nodes.
     * @param depth The depth at which to add the new row of nodes.
     *
     * @return The root node of the binary tree after adding the new row of nodes.
     */
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if (depth == 1) {
            return new TreeNode(val, root, null);
        }
        helper(root, val, depth, 1);
        return root;
    }

    /**
     * Recursive helper method to add a row of nodes at a specified depth in the binary tree.
     *
     * @param root         The current node in the binary tree.
     * @param val          The value for the new row of nodes.
     * @param depth        The depth at which to add the new row of nodes.
     * @param currentDepth The current depth in the binary tree.
     */
    private void helper(TreeNode root, int val, int depth, int currentDepth) {
        if (root == null) {
            return;
        }
        if (currentDepth == depth - 1) {
            root.left = new TreeNode(val, root.left, null);
            root.right = new TreeNode(val, null, root.right);
        } else {
            helper(root.left, val, depth, currentDepth + 1);
            helper(root.right, val, depth, currentDepth + 1);
        }
    }
}
