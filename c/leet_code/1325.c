/**
 * @file leet_code/1325.c
 * @brief This file contains the implementation of a function to remove leaf nodes from a binary tree.
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
 *
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 */

#pragma GCC optimize("O3,unroll-loops")

#include <stdlib.h>

/**
 * @struct TreeNode
 * @brief A structure to represent a node in a binary tree.
 *
 * This structure has an integer value and two pointers to the left and right child nodes.
 */
struct TreeNode {
    int val; /**< The value of the node */
    struct TreeNode *left; /**< Pointer to the left child node */
    struct TreeNode *right; /**< Pointer to the right child node */
};

/**
 * @typedef NodePtr
 * @brief Type definition for a pointer to a TreeNode
 *
 * This type is used to simplify the syntax of function signatures and variable declarations.
 */
typedef struct TreeNode *NodePtr;

/**
 * @brief A function to delete a target node from a binary tree.
 *
 * This function recursively traverses the binary tree and deletes the target node if found.
 * It first checks if the node is not NULL, then recursively calls itself for the left and right child nodes.
 * If the node is a leaf node (i.e., both left and right child nodes are NULL) and its value is equal to the target,
 * it frees the memory allocated for the node and sets the node pointer to NULL.
 *
 * @param node A pointer to the current node in the binary tree.
 * @param target The target value to delete from the binary tree.
 * @return A pointer to the node after deletion. If the node was deleted, it returns NULL.
 */
NodePtr target_delete(struct TreeNode *node, const int target) {
    if (node != NULL) {
        node->left = target_delete(node->left, target);
        node->right = target_delete(node->right, target);

        if (node->left == NULL && node->right == NULL && node->val == target) {
            free(node);
            node = NULL;
        }
    }
    return node;
}

/**
 * @brief A function to remove leaf nodes from a binary tree.
 *
 * This function calls the target_delete function to remove the leaf nodes from the binary tree.
 * It takes as input a pointer to the root node of the binary tree and the target value to delete.
 * It returns a pointer to the root node after deletion.
 *
 * @param root A pointer to the root node of the binary tree.
 * @param target The target value to delete from the binary tree.
 * @return A pointer to the root node after deletion.
 */
struct TreeNode* removeLeafNodes(struct TreeNode* root, const int target) {
    return target_delete(root, target);
}
