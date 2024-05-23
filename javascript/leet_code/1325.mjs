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
 * This file `1325.mjs` contains a class `TreeNode` and a function `removeLeafNodes`.
 * The `TreeNode` class is used to create a binary tree node with a value and optional left and right child nodes.
 * The `removeLeafNodes` function removes all the leaf nodes from a binary tree that have a value equal to a target
 * value.
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
 * Function to remove all the leaf nodes from a binary tree that have a value equal to a target value.
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @param {number} target - The target value.
 * @returns {TreeNode} - The root node of the binary tree after removing the leaf nodes with the target value.
 */
const removeLeafNodes = function (root, target) {
    // If the root node is null, return null.
    if (!root) {
        return root;
    }

    // Recursively call the function for the left and right child nodes of the root node.
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);

    // If the value of the root node is equal to the target value and the root node is a leaf node, return null.
    if (root.val === target && !root.left && !root.right) {
        return null;
    }

    // Return the root node.
    return root;
};
