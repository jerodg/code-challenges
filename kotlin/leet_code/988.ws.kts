/**
 * Represents a node in a binary tree.
 * Each node has a value and two children: left and right.
 */
class TreeNode(var value: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

/**
 * Contains methods to solve the problem.
 */
class Solution {
    /**
     * Returns the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
     *
     * @param root the root of the tree.
     * @return the lexicographically smallest string.
     */
    fun smallestFromLeaf(root: TreeNode?): String {
        return dfs(root, "")
    }

    /**
     * Performs a depth-first search (DFS) on the tree to find the lexicographically smallest string.
     *
     * @param node the current node.
     * @param s the current string.
     * @return the lexicographically smallest string.
     */
    private fun dfs(node: TreeNode?, s: String): String {
        // If the node is null, return the current string
        if (node == null) return s
        // Convert the node value to a character
        val c = 'a' + node.value
        // Prepend the character to the current string
        val s_ = c + s
        // If the node is a leaf, return the current string
        if (node.left == null && node.right == null) return s_
        // If the node has no left child, continue with the right child
        if (node.left == null) return dfs(node.right, s_)
        // If the node has no right child, continue with the left child
        if (node.right == null) return dfs(node.left, s_)
        // Perform DFS on the left child
        val s1 = dfs(node.left, s_)
        // Perform DFS on the right child
        val s2 = dfs(node.right, s_)
        // Return the lexicographically smallest string
        return if (s1 < s2) s1 else s2
    }
}
