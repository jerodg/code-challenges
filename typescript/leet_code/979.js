/*
 *  Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 *  This program is free software: you can redistribute it and/or modify it under the terms of the
 *  Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 *  or (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 *  even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 *  for more details.
 *
 *  The above copyright notice and this permission notice shall be included in all copies or
 *  substantial portions of the Software. You should have received a copy of the SSPL along with this
 *  program. If not, see SSPL.
 */
/**
 * Package leet_code
 *
 * This file contains the implementation of the `TreeNode` class and the `distributeCoins` function.
 * The `TreeNode` class represents a node in a binary tree.
 * The `distributeCoins` function redistributes the coins in the binary tree to make the number of coins at each node
 * equal to 1.
 */
/**
 * Class representing a node in a binary tree.
 */
var TreeNode = /** @class */ (function () {
    /**
     * Creates a new TreeNode instance.
     *
     * @param {number} [val=0] - The value of the node.
     * @param {TreeNode | null} [left=null] - The left child of the node.
     * @param {TreeNode | null} [right=null] - The right child of the node.
     */
    function TreeNode(val, left, right) {
        this.val = (val === undefined ? 0 : val);
        this.left = (left === undefined ? null : left);
        this.right = (right === undefined ? null : right);
    }
    return TreeNode;
}());
/**
 * Function to redistribute the coins in a binary tree to make the number of coins at each node equal to 1.
 *
 * @param {TreeNode | null} root - The root of the binary tree.
 * @returns {number} - The minimum number of moves required to redistribute the coins.
 *
 * @example
 *
 * const root = new TreeNode(3, new TreeNode(0), new TreeNode(0));
 * distributeCoins(root)
 * // returns 2
 */
function distributeCoins(root) {
    // Initialize the number of moves
    var moves = 0;
    /**
     * Recursive helper function to calculate the number of coins needed to make the number of coins at the current
     * node equal to 1.
     *
     * @param {TreeNode | null} current - The current node.
     * @returns {number} - The number of coins needed.
     */
    function dfs(current) {
        // If the current node is null, return 0
        if (current === null) {
            return 0;
        }
        // Calculate the number of coins needed for the left and right children
        var leftCoins = dfs(current.left);
        var rightCoins = dfs(current.right);
        // Update the number of moves
        moves += Math.abs(leftCoins) + Math.abs(rightCoins);
        // Return the number of coins needed for the current node
        return (current.val - 1) + leftCoins + rightCoins;
    }
    // Call the helper function with the root of the binary tree
    dfs(root);
    // Return the number of moves
    return moves;
}
