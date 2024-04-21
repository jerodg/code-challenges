/** This is the Solution object. It contains a method to add a row of nodes with a given value at a given depth in a binary tree.
  * The method returns the root of the modified tree.
  *
  * @example
  * val root = new TreeNode(4, new TreeNode(2, new TreeNode(3), new TreeNode(1)), new TreeNode(6, new TreeNode(5)))
  * val result = Solution.addOneRow(root, 1, 2)
  * // result: TreeNode(4, TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(1))), TreeNode(1, TreeNode(6, TreeNode(5))))
  *
  * @note The method modifies the input tree by adding a row of nodes at the specified depth.
  */
object Solution {

  /** Adds a row of nodes with a given value at a given depth in a binary tree.
    *
    * @param root The root of the binary tree.
    * @param `val` The value of the nodes to be added.
    * @param depth The depth at which the nodes should be added.
    * @return The root of the modified tree.
    * @throws IllegalArgumentException if the depth is less than 1.
    */
  def addOneRow(root: TreeNode, `val`: Int, depth: Int): TreeNode = {
    if (depth < 1) {
      throw new IllegalArgumentException("Depth must be greater than 0")
    }
    helper(root, `val`, depth, 1)
  }

  /** Helper function to recursively add nodes at a given depth in a binary tree.
    *
    * @param root The root of the binary tree.
    * @param `val` The value of the nodes to be added.
    * @param depth The depth at which the nodes should be added.
    * @param layer The current layer of the tree.
    * @return The root of the modified tree.
    */
  private def helper(
      root: TreeNode,
      `val`: Int,
      depth: Int,
      layer: Int
  ): TreeNode = {
    if (root == null) return null
    if (depth == 1) {
      val newNode = new TreeNode(_value = `val`, _left = root)
      return newNode
    }
    if (layer == depth - 1) {
      var newNode = new TreeNode(_value = `val`, _left = root.left)
      root.left = newNode
      newNode = new TreeNode(_value = `val`, _right = root.right)
      root.right = newNode
    } else {
      root.left = helper(root.left, `val`, depth, layer + 1)
      root.right = helper(root.right, `val`, depth, layer + 1)
    }
    root
  }
}
