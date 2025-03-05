"""Copyright ©2010-2025 JerodG <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

Provides a solution to LeetCode problem 988: Smallest String Starting From Leaf.

This module implements an algorithm that finds the lexicographically smallest string
obtained by following a path from a leaf to the root in a binary tree. Node values
are converted to lowercase letters (0 -> 'a', 1 -> 'b', etc.) and the resulting string
is reversed before comparison.

Example:
    >>> root = TreeNode(0, TreeNode(1), TreeNode(2))
    >>> Solution().smallestFromLeaf(root)
    'abc'
"""

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    """Represents a node in a binary tree.

    Each node contains a value and references to left and right children.

    Attributes:
        val: The value stored in this node.
        left: Reference to the left child node.
        right: Reference to the right child node.
    """
    val: int = 0
    left: 'TreeNode' = None
    right: 'TreeNode' = None


class Solution:
    """Solves the problem of finding the lexicographically smallest string from root to leaf.

    Converts each path from root to leaf into a string by mapping node values to lowercase letters
    (where 0 maps to 'a', 1 to 'b', etc.) and reversing the string.
    """
    def __init__(self):
        """Initializes a new Solution instance with an empty results list."""
        self.results: List[str] = []

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """Finds the lexicographically smallest string formed by a path from a leaf to the root.

        Uses depth-first search to traverse all paths from root to leaves, collects all
        possible strings, and returns the lexicographically smallest one.

        Args:
            root: The root node of the binary tree.

        Returns:
            The lexicographically smallest string formed by a path from a leaf to the root.

        Examples:
            >>> Solution().smallestFromLeaf(TreeNode(0, TreeNode(1), TreeNode(2)))
            'aab'
        """
        def fun(node: TreeNode, res: str) -> None:
            """Recursively traverses the tree and builds path strings from root to leaves.

            Args:
                node: The current node being visited.
                res: The accumulated path string from root to the current node.
            """
            if node.left:
                fun(node.left, res + chr(97 + node.val))

            if node.right:
                fun(node.right, res + chr(97 + node.val))

            # When reaching a leaf node, add the value and reverse the path string
            if not node.left and not node.right:
                res += chr(97 + node.val)
                self.results.append(res[::-1])

        fun(root, '')
        # Sort all path strings to find the lexicographically smallest one
        self.results.sort()

        return self.results[0]