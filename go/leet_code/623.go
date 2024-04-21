// Package leet_code provides solutions for LeetCode problems.
package leet_code

// TreeNode represents a node in a binary tree.
// Each node contains an integer value, a pointer to the left child node, and a pointer to the right child node.
type TreeNode struct {
	Val   int       // The value of the node.
	Left  *TreeNode // Pointer to the left child node.
	Right *TreeNode // Pointer to the right child node.
}

// addOneRow adds a row of nodes with a given value at a given depth in the binary tree.
// The original nodes at depth will be the left child of the new nodes.
// The root of the tree will be the new nodes if depth is 1.
// The new row will be inserted immediately below the root if depth is 2.
// If depth is greater than 2, the function is called recursively for the left and right child nodes with a decremented depth.
//
// Parameters:
//  - root: Pointer to the root node of the binary tree.
//  - val: The value for the new nodes.
//  - depth: The depth at which the new row should be added.
//
// Returns:
//  - Pointer to the root node of the modified binary tree.
//
// Error Handling:
//  - If the root is nil, the function returns nil.
//
// Example Usage:
//  root := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}
//  val := 4
//  depth := 2
//  newRoot := addOneRow(root, val, depth) // newRoot now points to the root of the modified tree.
func addOneRow(root *TreeNode, val int, depth int) *TreeNode {
	if root == nil {
		return nil
	}

	if depth == 1 {
		root = &TreeNode{Val: val, Left: root}
	} else if depth == 2 {
		root.Left = &TreeNode{Val: val, Left: root.Left}
		root.Right = &TreeNode{Val: val, Right: root.Right}
	} else {
		addOneRow(root.Left, val, depth-1)
		addOneRow(root.Right, val, depth-1)
	}
	return root
}
