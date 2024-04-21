// Package leet_code provides solutions for LeetCode problems.
package leet_code

import "math"

// TreeNode represents a node in a binary tree.
// Each node contains an integer value, a pointer to the left child node, and a pointer to the right child node.
type TreeNode struct {
	Val   int       // The value of the node.
	Left  *TreeNode // The left child of the node.
	Right *TreeNode // The right child of the node.
}

// addOneRow adds a row of nodes with a given value to a binary tree at a given depth.
// The root node is at depth 1, and the added row is at the given depth.
// If the depth is 1, a new root node is created with the given value, and the original tree becomes the left child of the new root.
// The function modifies the tree in place and returns the root of the modified tree.
//
// Parameters:
//   - root: The root node of the binary tree.
//   - val: The value of the nodes in the added row.
//   - depth: The depth at which to add the row.
//
// Returns:
//   - The root node of the modified tree.
//
// Example usage:
//   root := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}}
//   root = addOneRow(root, 3, 2)
//   // The tree now looks like this:
//   //     1
//   //    / \
//   //   3   3
//   //  /
//   // 2
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
	if depth == 1 {
		return &TreeNode{Val: val, Left: root}
	}
	var dfs func(*TreeNode, int)
	depth -= 1
	// dfs is a helper function that traverses the tree and adds the new row at the correct depth.
	dfs = func(node *TreeNode, level int) {
		if node == nil {
			return
		}
		if level < depth {
			dfs(node.Left, level+1)
			dfs(node.Right, level+1)
			return
		}
		// Add the new row by creating new nodes with the given value and making the original children of the current node the children of the new nodes.
		node.Left = &TreeNode{Val: val, Left: node.Left}
		node.Right = &TreeNode{Val: val, Right: node.Right}
	}
	dfs(root, 1)
	return root
}
