from typing import Optional


class TreeNode:
    """A class to represent a binary tree node.

    Attributes:
        val: An integer representing the value of the node.
        left: An instance of TreeNode representing the left child of the node.
        right: An instance of TreeNode representing the right child of the node.
    """

    def __init__(self, val=0, left=None, right=None):
        """Initializes TreeNode with a value and optional left and right children.

        Args:
            val: An integer representing the value of the node. Defaults to 0.
            left: An optional instance of TreeNode representing the left child of the node. Defaults to None.
            right: An optional instance of TreeNode representing the right child of the node. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """A class to represent the solution for adding a row to a binary tree."""

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        """Adds a row of nodes with a value v at the given depth d and returns the root of the updated tree.

        The original nodes of depth d are moved to be the children of the new nodes.

        If there is no node of depth d, the new row is inserted at the depth d and the original nodes of depth d-1 become the parents of the new nodes.

        Args:
            root: An instance of TreeNode representing the root of the binary tree.
            val: An integer representing the value of the new nodes.
            depth: An integer representing the depth at which to add the new row.

        Returns:
            The root of the updated tree.

        Raises:
            ValueError: If the depth is less than 1.

        Examples:
            >>> solution = Solution()
            >>> root = TreeNode(4, TreeNode(2, TreeNode(3), TreeNode(1)), TreeNode(6, None, TreeNode(5)))
            >>> solution.addOneRow(root, 1, 2)
            TreeNode(4, TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(1)), None), TreeNode(1, None, TreeNode(6, None, TreeNode(5))))
        """
        if depth < 1:
            raise ValueError('Depth must be greater than 0.')

        def dfs(root, val, depth):
            """Performs a depth-first search on the tree and adds new nodes at the specified depth."""
            if root is None:
                return
            if depth > 2:
                dfs(root.left, val, depth - 1)
                dfs(root.right, val, depth - 1)
            else:
                ptr = root.left
                root.left = TreeNode(val, ptr, None)

                ptr = root.right
                root.right = TreeNode(val, None, ptr)

        if depth == 1:
            ptr = TreeNode(val, root, None)
            return ptr
        dfs(root, val, depth)
        return root
