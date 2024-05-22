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
 * @file leet_code/979.c
 * @brief This file contains the implementation of the distributeCoins function.
 *
 * The function calculates the minimum number of moves to distribute the coins in a binary tree to each node.
 */
#pragma GCC optimize("O3,unroll-loops")

#include <stdlib.h>
#include <stdint.h>

/**
 * @brief Definition of the TreeNode structure.
 *
 * This structure represents a node in a binary tree. It contains an integer value and pointers to the left and right child nodes.
 */
struct TreeNode {
     int val; ///< The value of the node.
     struct TreeNode *left; ///< Pointer to the left child node.
     struct TreeNode *right; ///< Pointer to the right child node.
};

/**
 * @brief Recursive helper function to calculate the number of moves needed to distribute the coins.
 *
 * This function is used by the distributeCoins function to calculate the number of moves needed to distribute the coins in the binary tree.
 * It calculates the number of extra or deficient coins at each node and adds the absolute value of this number to the total number of moves.
 *
 * @param node The current node in the binary tree.
 * @param moves Pointer to the variable where the total number of moves is stored.
 * @return The number of extra or deficient coins at the current node.
 */
int16_t helper(const struct TreeNode* node, int16_t* moves) {
    if(node)   {
        const int16_t extra = (node->val + helper(node->left, moves) + helper(node->right, moves) - 1);
        *moves += abs(extra);
        return extra;
    }
    return 0;
}

/**
 * @brief Function to calculate the minimum number of moves to distribute the coins in a binary tree to each node.
 *
 * This function uses the helper function to calculate the number of moves needed to distribute the coins in the binary tree.
 * It initializes the number of moves to 0 and then calls the helper function with the root of the tree.
 *
 * @param root The root of the binary tree.
 * @return The minimum number of moves to distribute the coins.
 */
int distributeCoins(const struct TreeNode* root){
    int16_t moves = 0; // Variable to store the total number of moves.
    helper(root, &moves); // Call the helper function to calculate the number of moves.
    return moves; // Return the total number of moves.
}
