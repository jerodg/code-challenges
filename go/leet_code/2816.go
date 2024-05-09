/*
Package leet_code provides solutions for LeetCode problems.

Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify it under the terms of the
Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
for more details.

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software. You should have received a copy of the SSPL along with this
program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
*/
package leet_code

// ListNode represents a node in a singly-linked list.
type ListNode struct {
	Val  int       // Val represents the value of the node.
	Next *ListNode // Next points to the next node in the list.
}

// doubleIt takes a head of a linked list and doubles the value of each node in the list.
// It returns the head of the modified list.
func doubleIt(head *ListNode) *ListNode {
	q := calc(head)
	if q > 0 {
		return &ListNode{Val: q, Next: head}
	}
	return head
}

// calc is a helper function that recursively calculates the doubled value of each node in the list.
// It modifies the value of each node in the list and returns the carry for the next node.
func calc(node *ListNode) int {
	if node != nil {
		v := node.Val*2 + calc(node.Next)
		node.Val = v % 10

		return v / 10
	}
	return 0
}
