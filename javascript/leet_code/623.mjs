/**
 * @fileoverview This module provides a function to add a row to a binary tree.
 */

/**
 * TreeNode constructor function.
 * @constructor
 * @param {number} val - The value of the node.
 * @param {TreeNode} left - The left child of the node.
 * @param {TreeNode} right - The right child of the node.
 */
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

/**
 * Adds a row of nodes with a specified value to a binary tree at a specified depth.
 * @param {TreeNode} root - The root node of the binary tree.
 * @param {number} val - The value for the new row of nodes.
 * @param {number} depth - The depth at which to add the new row.
 * @return {TreeNode} The root node of the modified tree.
 */
let addOneRow = function (root, val, depth) {
    // If the specified depth is 1, create a new root node with the specified value
    // and the original tree as its left child.
    if (depth === 1) {
        return new TreeNode(val, root, null);
    }

    /**
     * Performs a depth-first search on the tree to find the nodes at the specified depth - 1.
     * @param {TreeNode} node - The current node.
     * @param {number} level - The current level.
     */
    const dfs = (node, level) => {
        // If the node is null, return.
        if (null === node) {
            return;
        }
        // If the current level is less than the specified depth - 1, continue the search.
        if (level < depth - 1) {
            dfs(node.left, level + 1);
            dfs(node.right, level + 1);
            return;
        }
        // Create new nodes with the specified value and the original children of the node.
        let leftNode = new TreeNode(val, node.left, null);
        let rightNode = new TreeNode(val, null, node.right);
        // Replace the original children of the node with the new nodes.
        node.left = leftNode;
        node.right = rightNode;
    };
    // Start the depth-first search.
    dfs(root, 1);

    // Return the root node of the modified tree.
    return root;
};
