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
 * This file `2331.mjs` contains a class `TreeNode` and a function `evaluateTree`.
 * The `TreeNode` class is used to create a binary tree node with a value and optional left and right child nodes.
 * The `evaluateTree` function evaluates the binary tree according to the following rules:
 * - If a node is a leaf (has no children), it is evaluated as true if its value is 1 and false otherwise.
 * - If a node has a value of 2, it is evaluated as the logical OR of its children.
 * - If a node has a value of 3, it is evaluated as the logical AND of its children.
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
 * Function to evaluate the binary tree according to the following rules:
 * - If a node is a leaf (has no children), it is evaluated as true if its value is 1 and false otherwise.
 * - If a node has a value of 2, it is evaluated as the logical OR of its children.
 * - If a node has a value of 3, it is evaluated as the logical AND of its children.
 *
 * @param {TreeNode} root - The root node of the binary tree.
 * @returns {boolean} - The result of the evaluation of the binary tree.
 */
const evaluateTree = function (root) {
    const node = root;

    // If the node is a leaf, return true if its value is 1 and false otherwise.
    if (node.left === null && node.right === null) {
        return node.val === 1;
    }
    // If the node has a value of 2, return the logical OR of the evaluation of its children.
    else if (node.val === 2) {
        return evaluateTree(node.left) || evaluateTree(node.right);
    }
    // If the node has a value of 3, return the logical AND of the evaluation of its children.
    else if (node.val === 3) {
        return evaluateTree(node.left) && evaluateTree(node.right);
    }
    // If the node has a value other than 1, 2, or 3, return false.
    return false;
};
