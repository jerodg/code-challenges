/**
 * @fileoverview This module provides solutions to various LeetCode problems. It includes functions for manipulating
 *     binary trees, checking the validity of strings with parentheses and asterisks, and rearranging arrays in a
 *     specific order.
 *
 * @module leet_code/988
 */

/**
 * TreeNode constructor function. Creates a new TreeNode object.
 *
 * @class
 * @param {number} val - The value of the node. Defaults to 0 if not provided.
 * @param {TreeNode} left - The left child of the node. Defaults to null if not provided.
 * @param {TreeNode} right - The right child of the node. Defaults to null if not provided.
 */
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

/**
 * This function finds the smallest string (in lexicographical order) that starts from a leaf of a binary tree and ends
 * at the root. The characters of the string are mapped from the values of the nodes (0 maps to 'a', 1 maps to 'b',
 * etc.).
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {string} - The smallest string that starts from a leaf and ends at the root.
 */
const smallestFromLeaf = function (root) {
    /** @type {string} */
    let smallestStr;

    /**
     * This helper function performs a depth-first search on the tree to find all the strings that start from
     * a leaf and end at the root.
     *
     * @param {TreeNode} root - The current node.
     * @param {string} currStr - The current string.
     */
    function dfs(root, currStr) {
        // If the node is null, return.
        if (root === null) {
            return;
        }

        // Add the character mapped from the value of the node to the start of the current string.
        currStr = String.fromCharCode("a".charCodeAt(0) + root.val) + currStr;

        // If the node is a leaf, compare the current string with the smallest string found so far.
        if (root.left === null && root.right == null) {
            if (!smallestStr) {
                smallestStr = currStr;
            } else {
                if (currStr < smallestStr) {
                    smallestStr = currStr;
                }
            }
            return;
        }
        // Continue the search on the left and right children of the node.
        dfs(root.left, currStr);
        dfs(root.right, currStr);
    }

    // Start the depth-first search.
    dfs(root, "");
    // Return the smallest string found.
    return smallestStr;
};
