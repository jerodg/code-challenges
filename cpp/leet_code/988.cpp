// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <iostream>
#include <string>

// Solution class
class Solution {
public:
    // Member variable to store the answer
    std::string ans;

    /**
     * Function to find the smallest string from leaf to root in a binary tree.
     * @param node: Pointer to the current TreeNode.
     * @param temp: Reference to the string representing the current path.
     */
    void FindSmallest(const TreeNode *node, std::string &temp) {
        // Append the current character represented by the node's value to the path.
        temp += ('a' + node->val);

        // If the current node is a leaf node
        if (!node->left && !node->right) {
            // Reverse the current path to get the path from leaf to root.
            const std::string final_string(temp.rbegin(), temp.rend());

            // If ans is empty or final_string is smaller than ans, update ans.
            if (ans.empty() || final_string < ans) {
                ans = final_string;
            }
        }

        // If the current node has a left child, continue the traversal on the left subtree.
        if (node->left) {
            FindSmallest(node->left, temp);
            temp.pop_back(); // Backtrack
        }

        // If the current node has a right child, continue the traversal on the right subtree.
        if (node->right) {
            FindSmallest(node->right, temp);
            temp.pop_back(); // Backtrack
        }
    }

    /**
     * Function to find the lexicographically smallest string from leaf to root in a binary tree.
     * @param root: Pointer to the root of the binary tree.
     * @return The lexicographically smallest string from leaf to root.
     */
    std::string smallestFromLeaf(const TreeNode *root) {
        // Improve the performance of cin
        std::ios_base::sync_with_stdio(false);
        std::cin.tie(nullptr);

        // String to store the current path
        std::string temp;

        // Start the traversal from the root
        FindSmallest(root, temp);

        // Return the smallest string from leaf to root
        return ans;
    }
};
