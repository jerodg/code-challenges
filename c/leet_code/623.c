/**
 * @file leet_code/623.c
 * @brief This file contains the implementation of the addOneRow function.
 *
 * The function adds a row of nodes with a given value to a binary tree at a given depth.
 * The original nodes at the depth are moved down to become the left child of the new nodes.
 * The function uses a helper function to recursively traverse the tree and add the new nodes.
 *
 */

#include <stdlib.h>  // Required for dynamic memory allocation functions

/**
 * @struct TreeNode
 * @brief A structure to represent a node in a binary tree.
 *
 * This structure has an integer value and two pointers to other nodes in the tree.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/**
 * @brief Creates a new node with a given value.
 *
 * This function allocates memory for a new node, sets its value to the given data,
 * and initializes its left and right pointers to NULL.
 *
 * @param data The value to be stored in the new node.
 * @return A pointer to the new node.
 */
struct TreeNode *create(const int data) {
    struct TreeNode *newnode = (struct TreeNode *) malloc(sizeof(struct TreeNode));
    newnode->val = data;
    newnode->left = NULL;
    newnode->right = NULL;
    return newnode;
}

/**
 * @brief Recursively adds a row of nodes to a binary tree at a given depth.
 *
 * This function is a helper function for the addOneRow function.
 * It recursively traverses the tree and adds a row of nodes with a given value at a given depth.
 * The original nodes at the depth are moved down to become the left child of the new nodes.
 *
 * @param depth1 The current depth in the tree.
 * @param depth The depth at which the new row should be added.
 * @param root A pointer to the current node in the tree.
 * @param val The value to be stored in the new nodes.
 */
void fun1(const int depth1, const int depth, struct TreeNode *root, const int val) {
    if (root == NULL) {
        return;
    }
    if (depth1 == depth - 1) {
        struct TreeNode *left = root->left;
        struct TreeNode *right = root->right;

        struct TreeNode *node_left = create(val);
        struct TreeNode *node_right = create(val);

        node_left->left = left;
        node_right->right = right;
        root->left = node_left;
        root->right = node_right;
        return;
    }
    fun1(depth1 + 1, depth, root->left, val);
    fun1(depth1 + 1, depth, root->right, val);
}

/**
 * @brief Adds a row of nodes with a given value to a binary tree at a given depth.
 *
 * This function adds a row of nodes with a given value to a binary tree at a given depth.
 * The original nodes at the depth are moved down to become the left child of the new nodes.
 * The function uses the fun1 helper function to recursively traverse the tree and add the new nodes.
 *
 * @param root A pointer to the root of the tree.
 * @param val The value to be stored in the new nodes.
 * @param depth The depth at which the new row should be added.
 * @return A pointer to the root of the tree after the new row has been added.
 */
struct TreeNode *addOneRow(struct TreeNode *root, const int val, const int depth) {
    if (depth == 1) {
        struct TreeNode *node = create(val);
        node->left = root;
        return node;
    } else {
        fun1(1, depth, root, val);
        return root;
    }
}
