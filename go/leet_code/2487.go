// leet_code/2487.go
// This file contains the implementation of a linked list and functions to manipulate it.
// Author: jerodg <https://github.com/jerodg/>

package leet_code

// ListNode represents a node in a singly linked list.
type ListNode struct {
	Val  int       // Val is the value of the node.
	Next *ListNode // Next is a pointer to the next node in the list.
}

// removeNodes removes nodes from the list that have a greater value than the next node.
// It first reverses the list, removes the nodes, and then reverses the list again.
// It returns the head of the modified list.
func removeNodes(head *ListNode) *ListNode {
	head = reverseList(head)
	temp := head
	for temp != nil {
		if temp.Next != nil && temp.Val > temp.Next.Val {
			temp.Next = temp.Next.Next
		} else {
			temp = temp.Next
		}
	}
	return reverseList(head)
}

// reverseList reverses the order of nodes in the list.
// It returns the head of the reversed list.
func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	for head != nil {
		next := head.Next
		head.Next = prev
		prev, head = head, next
	}
	return prev
}
