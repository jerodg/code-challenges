/**
 * @file leet_code/2331.c
 * @brief This file contains the implementation of a binary tree structure and a
 *        function to evaluate the tree.
 *
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the Server Side Public License (SSPL) as published by MongoDB, Inc.,
 * either version 1 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 * or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL for more details.
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software. You should have received a
 * copy of the SSPL along with this program. If not, see SSPL.
 */

#pragma GCC optimize("O3,unroll-loops")

/**
 * @struct TreeNode
 * @brief A structure to represent a node in a binary tree.
 *
 * Each node has an integer value and two pointers to its left and right children.
 */
struct TreeNode {
     int val; /**< The value of the node. */
     struct TreeNode *left; /**< Pointer to the left child of the node. */
     struct TreeNode *right; /**< Pointer to the right child of the node. */
};

/**
 * @brief Evaluates a binary tree according to specific rules.
 *
 * This function traverses the tree in a depth-first manner. The evaluation rules
 * are as follows:
 * - If the node's value is 0 or 1, the function returns the node's value.
 * - If the node's value is 2, the function returns 1 if either of the node's
 * children evaluates to 1, otherwise it returns 0.
 * - For any other node value, the function returns 1 if both of the node's
 * children evaluate to 1, otherwise it returns 0.
 *
 * @param root A pointer to the root of the tree.
 * @return The result of the evaluation as a boolean value.
 */
bool evaluateTree(const struct TreeNode* root) {
    if (root->val == 0 || root->val == 1) {
        return root->val;
    }
    if (root->val == 2) {
        if ((evaluateTree(root->left) == 1) || (evaluateTree(root->right) == 1)) {
            return 1;
        }
        return 0;
    }
    if ((evaluateTree(root->left) == 1) && (evaluateTree(root->right) == 1)) {
        return 1;
    }
    return 0;
}
