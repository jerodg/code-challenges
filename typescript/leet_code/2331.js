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
 * This file contains the implementation of the `TreeNode` class and the `evaluateTree` function.
 * The `TreeNode` class represents a node in a binary tree.
 * The `evaluateTree` function evaluates a binary tree based on certain conditions.
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
 * Function to evaluate a binary tree based on certain conditions.
 *
 * @param {TreeNode | null} root - The root of the binary tree.
 * @returns {boolean} - Returns `true` if the binary tree meets the conditions, `false` otherwise.
 *
 * The function performs a depth-first search on the binary tree.
 * If a node has both left and right children, the function checks the value of the node.
 * If the value is 2, the function performs a bitwise OR operation on the values of the left and right children and
 *     assigns the result to the node. If the value is not 2, the function performs a logical AND operation on the
 *     values of the left and right children and assigns the result to the node. The function returns the boolean value
 *     of the root node's value.
 */
function evaluateTree(root) {
    if (root.left) {
        evaluateTree(root.left);
    }
    if (root.right) {
        evaluateTree(root.right);
    }
    if (root.left && root.right) {
        if (root.val === 2) {
            root.val = root.left.val | root.right.val;
        }
        else {
            root.val = root.left.val && root.right.val;
        }
    }
    return !!root.val;
}
