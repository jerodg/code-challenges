/**
 * @file 1325.cpp
 * @brief This file contains a solution for removing leaf nodes from a binary tree that have a specific target value.
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
    int val; ///< The value of the node.
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
 * @brief This class contains a solution for removing leaf nodes from a binary tree that have a specific target value.
 */
class Solution {
public:
    /**
     * @brief Removes all leaf nodes from a binary tree that have a specific target value.
     *
     * This function uses a recursive approach to traverse the tree and remove the target nodes.
     *
     * @param root Pointer to the root node of the binary tree.
     * @param target The target value to remove from the tree.
     * @return Pointer to the root node of the modified tree.
     */
    static TreeNode* removeLeafNodes(TreeNode* root, const int target) {
        if(!root)
            return nullptr;

        // If the node is a leaf node and its value is equal to the target, remove it.
        if(!root->left && !root->right){
            if(root->val == target)
                return nullptr;
            else
                return root;
        }

        // Recursively remove target nodes from the left and right subtrees.
        root->left = removeLeafNodes(root->left, target);
        root->right = removeLeafNodes(root->right, target);

        // If the node is now a leaf node and its value is equal to the target, remove it.
        if(root->val == target && !root->left && !root->right)
            return nullptr;

        return root;
    }
};
