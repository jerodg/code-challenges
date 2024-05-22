/**
 * @file 2331.cpp
 * @brief This file contains a solution for evaluating a binary tree based on its node values.
 * @copyright Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
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
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */

#pragma GCC optimize("O3,unroll-loops")

/**
 * @class TreeNode
 * @brief This class represents a node in a binary tree.
 *
 * Each node contains an integer value and pointers to its left and right child nodes.
 */
struct TreeNode {
    int val; ///< The value of the node. This value is used to evaluate the tree.
    TreeNode *left; ///< Pointer to the left child node.
    TreeNode *right; ///< Pointer to the right child node.

    /**
     * @brief Default constructor. Initializes the node with a value of 0 and no child nodes.
     */
    TreeNode() : val(0), left(nullptr), right(nullptr) {}

    /**
     * @brief Constructor. Initializes the node with a given value and no child nodes.
     * @param x The value to initialize the node with.
     */
    explicit TreeNode(const int x) : val(x), left(nullptr), right(nullptr) {}

    /**
     * @brief Constructor. Initializes the node with a given value and child nodes.
     * @param x The value to initialize the node with.
     * @param left Pointer to the left child node.
     * @param right Pointer to the right child node.
     */
    TreeNode(const int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/**
 * @class Solution
 * @brief This class contains a solution for evaluating a binary tree based on its node values.
 */
class Solution {
public:
    /**
     * @brief Evaluates a binary tree based on its node values.
     *
     * This function uses a recursive approach to traverse the tree and evaluate it.
     * The evaluation rules are as follows:
     * - If the node value is 1, the result is true.
     * - If the node value is 0, the result is false.
     * - If the node value is 2, the result is the logical OR of the evaluations of the left and right child nodes.
     * - If the node value is 3, the result is the logical AND of the evaluations of the left and right child nodes.
     *
     * @param root Pointer to the root node of the binary tree.
     * @return The result of the evaluation.
     */
    static auto evaluateTree(const TreeNode* root)-> bool {
        if(root->val == 1)
            return true;
        if(root->val == 0)
            return false;
        if(root->val == 2)
            return evaluateTree(root->left) or evaluateTree(root->right);

        if(root->val == 3)
            return evaluateTree(root->left) and evaluateTree (root->right);

        return true;
    }
};
