import scala.annotation.tailrec

/**
  * This object contains a solution for finding the smallest string starting from leaf of a binary tree.
  * The characters of the string are formed by the values of the nodes, where a value of 0 corresponds to 'a', 1 corresponds to 'b', and so on.
  */
object Solution {

  /**
    * Definition for a binary tree node.
    * @param _value The value of the node, default is 0.
    * @param _left The left child of the node, default is null.
    * @param _right The right child of the node, default is null.
    */
  class TreeNode(_value: Int = 0, _left: TreeNode = null, _right: TreeNode = null) {
    var value: Int = _value
    var left: TreeNode = _left
    var right: TreeNode = _right
  }

  /**
    * Finds the smallest string starting from leaf of a binary tree.
    * @param root The root node of the binary tree.
    * @return The smallest string starting from leaf.
    */
  def smallestFromLeaf(root: TreeNode): String = {

    /**
      * Performs a depth-first search on the binary tree.
      * @param node The current node.
      * @param path The path from root to the current node.
      * @return The smallest string starting from leaf of the subtree rooted at the current node.
      */
    @tailrec
    def dfs(node: TreeNode, path: List[Char]): List[Char] = {
      if (node == null) return Nil
      // If the node is a leaf, return the string formed by the path from root to this leaf.
      if (node.left == null && node.right == null) return (node.value + 'a').toChar :: path
      val left: List[Char] = dfs(node.left, (node.value + 'a').toChar :: path)
      val right: List[Char] = dfs(node.right, (node.value + 'a').toChar :: path)
      // If one of the subtrees is empty, return the string from the other subtree.
      // Otherwise, return the smaller string.
      if (left.isEmpty) right
      else if (right.isEmpty) left
      else if (left.mkString < right.mkString) left
      else right
    }

    dfs(root, Nil).mkString
  }
}
