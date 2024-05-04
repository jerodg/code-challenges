/** This module defines a binary tree and a solution to find the smallest string starting from the leaf of the tree.
  * Each node in the tree contains a value which is an integer between 0 and 25, inclusive, representing the letters 'a' to 'z'.
  * The smallest string is the lexicographically smallest string that starts at any leaf of this tree and ends at its root.
  */

/** Class representing a node in a binary tree.
  *
  * @constructor create a new tree node with a value, left child, and right child.
  * @param _value the value of the node, an integer between 0 and 25, inclusive, representing the letters 'a' to 'z'.
  * @param _left the left child of the node, another TreeNode instance or null if there is no left child.
  * @param _right the right child of the node, another TreeNode instance or null if there is no right child.
  */
class TreeNode(
    _value: Int = 0,
    _left: TreeNode = null,
    _right: TreeNode = null
) {
  var value: Int = _value
  var left: TreeNode = _left
  var right: TreeNode = _right
}

/** Object containing the solution to find the smallest string starting from the leaf of the tree.
  */
object Solution {

  /** Function to find the smallest string starting from the leaf of the tree.
    *
    * @param root the root of the tree, a TreeNode instance.
    * @param prevMin the smallest string found so far, a string.
    * @return the smallest string starting from the leaf of the tree and ending at its root.
    */
  def smallestFromLeaf(root: TreeNode, prevMin: String = ""): String = {
    val nextMin: String = (root.value + 'a').toChar +: prevMin
    (root.left, root.right) match {
      case (null, null)  => nextMin
      case (left, null)  => smallestFromLeaf(left, nextMin)
      case (null, right) => smallestFromLeaf(right, nextMin)
      case (left, right) =>
        Ordering.String.min(
          smallestFromLeaf(left, nextMin),
          smallestFromLeaf(right, nextMin)
        )
    }
  }
}
