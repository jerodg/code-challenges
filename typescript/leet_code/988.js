/**
 * @fileoverview This module provides a class to represent a tree node and a function to find the smallest string
 *     starting from leaf.
 * @module leet_code/988
 */
/**
 * Class representing a tree node.
 */
const TreeNode = /** @class */ (function() {
  /**
     * Create a tree node.
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
 * Function to find the smallest string starting from leaf.
 * The function uses a depth-first search approach to traverse the tree.
 *
 * @param {TreeNode | null} root - The root of the tree.
 * @return {string} - The smallest string starting from leaf.
 * @throws {Error} - Throws an error if the input parameter is not valid.
 */
function smallestFromLeaf(root) {
  // Check if the input parameter is valid
  if (root === null) {
    throw new Error('Invalid input parameter');
  }
  let answer = '';

  /**
     * Helper function to perform depth-first search on the tree.
     *
     * @param {TreeNode} node - The current node.
     * @param {string} str - The current string.
     */
  function dfs(node, str) {
    const char = String.fromCharCode(node.val + 'a'.charCodeAt(0));
    // If the node is a leaf, update the answer if necessary
    if (node.left === null && node.right === null) {
      if (answer === '' || char + str < answer) {
        answer = char + str;
      }
      return;
    }
    // Recurse on the left child if it exists
    if (node.left) {
      dfs(node.left, char + str);
    }
    // Recurse on the right child if it exists
    if (node.right) {
      dfs(node.right, char + str);
    }
  }

  // Start the depth-first search from the root
  dfs(root, '');
  return answer;
}
