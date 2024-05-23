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

/**
 * Package leet_code
 *
 * This file `979.mjs` contains a class `TreeNode` and a function `distributeCoins`.
 * The `TreeNode` class is used to create a binary tree node with a value and optional left and right child nodes.
 * The `distributeCoins` function distributes the coins in the binary tree to make the number of coins in each node
 * equal to 1.
 */

/**
 * Class representing a node in a binary tree.
 */
function TreeNode(val, left, right) {
    /**
     * The value of the node.
     * @type {number}
     */
    this.val = val === undefined ? 0 : val;

    /**
     * The left child of the node.
     * @type {TreeNode}
     */
    this.left = left === undefined ? null : left;

    /**
     * The right child of the node.
     * @type {TreeNode}
     */
    this.right = right === undefined ? null : right;
}

/**
 * Function to distribute the coins in the binary tree to make the number of coins in each node equal to 1.
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {number} - The number of moves required to distribute the coins.
 */
const distributeCoins = function (root) {
    /**
     * The number of moves required to distribute the coins.
     * @type {number}
     */
    let moves = 0;

    /**
     * Helper function to recursively distribute the coins.
     *
     * @param {TreeNode} node - The current node.
     * @returns {number} - The number of coins that need to be moved from or to the parent of the node.
     */
    function dfs(node) {
        // If the node is null, return 0.
        if (node === null) {
            return 0;
        }

        // Recursively distribute the coins in the left and right child nodes.
        let left = dfs(node.left);
        let right = dfs(node.right);

        // Update the number of moves by the absolute values of the number of coins that need to be moved from or to
        // the left and right child nodes.
        moves += Math.abs(left) + Math.abs(right);

        // Return the number of coins that need to be moved from or to the parent of the node.
        return node.val + left + right - 1;
    }

    // Start the distribution of coins from the root node.
    dfs(root);

    // Return the number of moves required to distribute the coins.
    return moves;
};
