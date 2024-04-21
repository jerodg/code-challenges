/**
 * @file 623.cpp
 * @brief Contains the implementation of the TreeNode structure and Solution class.
 *
 * This file contains the implementation of a TreeNode structure which represents a node in a binary tree and a Solution class
 * which provides methods to manipulate the binary tree.
 */

#include <cstddef> // For nullptr

/**
 * @struct TreeNode
 * @brief A structure representing a node in a binary tree.
 *
 * This structure represents a node in a binary tree. Each node contains an integer value and pointers to its left and right children.
 */
struct TreeNode {
    int val; ///< The value stored in the node.
    TreeNode *left; ///< Pointer to the left child of the node.
    TreeNode *right; ///< Pointer to the right child of the node.

    /**
     * @brief Default constructor.
     *
     * Initializes the node with a value of 0 and no children.
     */
    TreeNode() : val(0), left(nullptr), right(nullptr) {
    }

    /**
     * @brief Constructor with value.
     *
     * Initializes the node with a given value and no children.
     *
     * @param x The value to initialize the node with.
     */
    explicit TreeNode(const int x) : val(x), left(nullptr), right(nullptr) {
    }

    /**
     * @brief Constructor with value and children.
     *
     * Initializes the node with a given value and pointers to its left and right children.
     *
     * @param x The value to initialize the node with.
     * @param left Pointer to the left child of the node.
     * @param right Pointer to the right child of the node.
     */
    TreeNode(const int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {
    }
};

/**
 * @class Solution
 * @brief A class providing methods to manipulate a binary tree.
 *
 * This class provides static methods to manipulate a binary tree represented by TreeNode structures.
 */
class Solution {
public:
    /**
     * @brief Recursive helper function to add a row to the binary tree.
     *
     * This function is used by the addOneRow method to recursively traverse the binary tree and add a row at a specified depth.
     *
     * @param root The root of the binary tree.
     * @param depth The current depth in the binary tree.
     * @param maxDepth The depth at which to add the new row.
     * @param val The value to use for the nodes in the new row.
     */
    static void func(TreeNode *root, const int depth, const int maxDepth, const int val);

    /**
     * @brief Adds a row to the binary tree at a specified depth.
     *
     * This method adds a row of nodes with a specified value to the binary tree at a specified depth.
     *
     * @param root The root of the binary tree.
     * @param val The value to use for the nodes in the new row.
     * @param depth The depth at which to add the new row.
     * @return The root of the modified binary tree.
     */
    static TreeNode *addOneRow(TreeNode *root, const int val, const int depth);
};

/**
 * @brief Implementation of the recursive helper function to add a row to the binary tree.
 *
 * This function is used by the addOneRow method to recursively traverse the binary tree and add a row at a specified depth.
 *
 * @param root The root of the binary tree.
 * @param depth The current depth in the binary tree.
 * @param maxDepth The depth at which to add the new row.
 * @param val The value to use for the nodes in the new row.
 */
auto Solution::func(TreeNode *root, const int depth, const int maxDepth, const int val) -> void {
    if (root == nullptr) return; // Base case: if the node is null, return.

    // If the current depth is one less than the max depth, add the new row.
    if (depth == maxDepth - 1) {
        TreeNode *l = nullptr;
        TreeNode *r = nullptr;
        if (root->left) {
            l = root->left;
        }
        if (root->right) {
            r = root->right;
        }
        root->left = new TreeNode(val);
        root->right = new TreeNode(val);

        root->left->left = l;
        root->right->right = r;
    }

    // If the current depth is less than the max depth, continue the recursion.
    if (depth < maxDepth - 1) {
        func(root->left, depth + 1, maxDepth, val);
        func(root->right, depth + 1, maxDepth, val);
    }
}

/**
 * @brief Adds a row to the binary tree at a specified depth.
 *
 * This method adds a row of nodes with a specified value to the binary tree at a specified depth.
 *
 * @param root The root of the binary tree.
 * @param val The value to use for the nodes in the new row.
 * @param depth The depth at which to add the new row.
 * @return The root of the modified binary tree.
 */
auto Solution::addOneRow(TreeNode *root, const int val, const int depth) -> TreeNode* {
    if (depth == 1) {
        const auto newRoot = new TreeNode(val);
        newRoot->left = root;
        return newRoot;
    }
    func(root, 1, depth, val); //pass value correctly
    return root;
}
