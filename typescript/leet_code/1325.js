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
 * This file contains the implementation of the `TreeNode` class and the `removeLeafNodes` function.
 * The `TreeNode` class represents a node in a binary tree.
 * The `removeLeafNodes` function removes all the leaf nodes with a specific value from a binary tree.
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
 * Function to remove all the leaf nodes with a specific value from a binary tree.
 *
 * @param {TreeNode | null} root - The root of the binary tree.
 * @param {number} target - The value of the leaf nodes to be removed.
 * @returns {TreeNode | null} - The root of the binary tree after removing the leaf nodes.
 */
function removeLeafNodes(root, target) {
    // If the root is null, return null
    if (!root) {
        return null;
    }
    // Recursively remove the leaf nodes from the left and right subtrees
    root.left = removeLeafNodes(root.left, target);
    root.right = removeLeafNodes(root.right, target);
    // If the root is a leaf node with the target value, remove it
    if (!root.left && !root.right && root.val === target) {
        return null;
    }
    // Return the root
    return root;
}
