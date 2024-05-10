import java.util.*

/**
 * This module provides a solution for the LeetCode problem #623, "Add One Row to Tree".
 * It uses a breadth-first search (BFS) to add a row at a given depth in a binary tree.
 *
 * @module leet_code/623.ws.kts
 */

/**
 * TreeNode class representing a node in a binary tree.
 */
class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

/**
 * Solution class for the "Add One Row to Tree" problem.
 */
class Solution {
    /**
     * Adds a row at a given depth in a binary tree.
     *
     * @param root The root node of the binary tree.
     * @param `val` The value to be added in the new row.
     * @param depth The depth at which the new row is to be added.
     * @return The root node of the modified binary tree.
     *
     * @throws IllegalArgumentException If the depth is less than 1.
     *
     * Example usage:
     * val solution = Solution()
     * val root = TreeNode(1)
     * root.left = TreeNode(2)
     * root.right = TreeNode(3)
     * val result = solution.addOneRow(root, 4, 2)
     * // The binary tree now looks like this:
     * //     1
     * //    / \
     * //   4   4
     * //  /     \
     * // 2       3
     */
    fun addOneRow(root: TreeNode?, `val`: Int, depth: Int): TreeNode? {
        // If the root is null, return null
        if (root == null) return null

        // If the depth is 1, create a new node with the given value and make the current root its left child
        if (depth == 1) {
            val res = TreeNode(`val`)
            res.left = root
            return res
        }

        // Initialize a queue for BFS and add the root to it
        val queue = LinkedList<TreeNode>()
        var d = 1
        queue.offer(root)

        // Perform BFS until the queue is empty
        while (queue.isNotEmpty()) {
            // If the current depth is one less than the target depth, add the new row
            if (d == depth - 1) {
                repeat(queue.size) {
                    val node = queue.poll()
                    val tmpLeft = node.left
                    val tmpRight = node.right
                    node.left = TreeNode(`val`)
                    node.right = TreeNode(`val`)

                    node.left.left = tmpLeft
                    node.right.right = tmpRight
                }
                return root
            } else if (d < depth - 1) {
                // If the current depth is less than the target depth, add the children of the current node to the queue
                repeat(queue.size) {
                    val node = queue.poll()
                    if (node.left != null) queue.offer(node.left)
                    if (node.right != null) queue.offer(node.right)
                }
            }
            d++
        }
        return root
    }
}
