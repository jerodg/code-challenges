/**
 * @fileoverview This module provides a TreeNode class and functions to add a row to a binary tree.
 * @module leet_code/623
 */
/**
 * Class representing a node in a binary tree.
 */
var TreeNode = /** @class */ (function () {
    /**
     * Create a new tree node.
     * @param {number} val - The value of the node.
     * @param {TreeNode | null} left - The left child of the node.
     * @param {TreeNode | null} right - The right child of the node.
     */
    function TreeNode(val, left, right) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
    }
    return TreeNode;
}());
/**
 * Function to add a row to a binary tree.
 * The function creates a new root node with the given value if the depth is 1.
 * Otherwise, it traverses the tree and adds the new row at the specified depth.
 *
 * @param {TreeNode | null} root - The root of the binary tree.
 * @param {number} val - The value for the new row.
 * @param {number} depth - The depth at which to add the new row.
 * @returns {TreeNode | null} - The root of the modified binary tree.
 */
function addOneRow(root, val, depth) {
    if (depth === 1) {
        return new TreeNode(val, root, null);
    }
    traverse(root, val, depth, 1);
    return root;
}
/**
 * Helper function to traverse the binary tree and add a new row at the specified depth.
 * The function recursively traverses the tree and when it reaches the specified depth, it adds a new node to the left and right of the current node.
 *
 * @param {TreeNode | null} node - The current node.
 * @param {number} val - The value for the new row.
 * @param {number} depth - The depth at which to add the new row.
 * @param {number} currentDepth - The current depth.
 */
function traverse(node, val, depth, currentDepth) {
    if (node == null) {
        return;
    }
    if (currentDepth + 1 === depth) {
        node.left = new TreeNode(val, node.left, null);
        node.right = new TreeNode(val, null, node.right);
        return;
    }
    traverse(node.left, val, depth, currentDepth + 1);
    traverse(node.right, val, depth, currentDepth + 1);
}
