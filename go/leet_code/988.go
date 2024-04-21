// Package leet_code provides solutions for LeetCode problems.
package leet_code

// Importing the fmt package for string formatting
import "fmt"

// TreeNode represents a node in a binary tree.
// Each node contains an integer value, a pointer to the left child node, and a pointer to the right child node.
type TreeNode struct {
	Val   int       // The value of the node.
	Left  *TreeNode // Pointer to the left child node.
	Right *TreeNode // Pointer to the right child node.
}

// Global variable to store the result string
var result string

// travel is a helper function that traverses the binary tree in a pre-order manner (root, left, right).
// It constructs strings from the node values and keeps track of the smallest string seen so far.
//
// Parameters:
//  - node: The current node being visited.
//  - s: The string constructed so far.
//
// Returns:
//  - None. The result is stored in the global variable 'result'.
//
// Error Handling:
//  - If the node is nil, the function returns without doing anything.
//
// Example Usage:
//  root := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}
//  s := ""
//  travel(root, s) // The result is stored in the global variable 'result'.
func travel(node *TreeNode, s string) {
	if node == nil {
		return
	}

	// Prepend the current node's value to the string
	s = fmt.Sprintf("%c", node.Val+97) + s

	// If the node is a leaf node, update the result
	if node.Left == nil && node.Right == nil {
		if result == "" {
			result = s
		} else {
			result = min(result, s)
		}
		return
	}

	// Recursively call the function for the left and right child nodes
	if node.Left != nil {
		travel(node.Left, s)
	}
	if node.Right != nil {
		travel(node.Right, s)
	}
}

// smallestFromLeaf finds the smallest string that starts from a leaf of a binary tree and ends at the root.
// The string is constructed by concatenating the characters corresponding to the node values in the path from the leaf to the root.
// The characters are determined by adding 97 to the node value to get the corresponding lowercase ASCII character.
//
// Parameters:
//  - root: The root node of the binary tree.
//
// Returns:
//  - The smallest string that starts from a leaf and ends at the root.
//
// Error Handling:
//  - If the root is nil, the function returns an empty string.
//
// Example Usage:
//  root := &TreeNode{Val: 1, Left: &TreeNode{Val: 2}, Right: &TreeNode{Val: 3}}
//  smallestString := smallestFromLeaf(root) // smallestString now contains the smallest string from leaf to root.
func smallestFromLeaf(root *TreeNode) string {
	// Reset the result
	result = ""

	// Call the helper function to traverse the tree and find the smallest string
	travel(root, "")

	// Return the result
	return result
}
