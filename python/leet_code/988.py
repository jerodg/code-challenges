from typing import Optional, List
from dataclasses import dataclass


@dataclass
class TreeNode:
    """Definition for a binary tree node."""
    val: int = 0
    left: 'TreeNode' = None
    right: 'TreeNode' = None


class Solution:
    """Solution for finding the smallest string starting from leaf of a binary tree."""

    def __init__(self):
        self.results: List[str] = []

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """
        Returns the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

        Args:
            root (Optional[TreeNode]): The root node of the tree.

        Returns:
            str: The lexicographically smallest string from leaf to root.

        Doctest:
            >>> tree = TreeNode(0)
            >>> tree.left = TreeNode(1)
            >>> tree.right = TreeNode(2)
            >>> s = Solution()
            >>> s.smallestFromLeaf(tree)
            'b'
            >>> tree.left.left = TreeNode(3)
            >>> tree.left.right = TreeNode(4)
            >>> s.smallestFromLeaf(tree)
            'dba'
            >>> tree.right.left = TreeNode(3)
            >>> tree.right.right = TreeNode(4)
            >>> s.smallestFromLeaf(tree)
            'dba'
        """

        def fun(node: TreeNode, res: str) -> None:
            """Helper function to traverse the tree and collect all strings from leaf to root."""
            if node.left:
                fun(node.left, res + chr(97 + node.val))

            if node.right:
                fun(node.right, res + chr(97 + node.val))

            if not node.left and not node.right:
                res += chr(97 + node.val)
                self.results.append(res[::-1])

        fun(root, '')
        self.results.sort()

        return self.results[0]
