// Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
//
// This program is free software: you can redistribute it and/or modify it under the terms of the
// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
// or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
// for more details.
//
// The above copyright notice and this permission notice shall be included in all copies or
// substantial portions of the Software. You should have received a copy of the SSPL along with this
// program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

/// `ListNode` is a struct that represents a node in a singly linked list.
/// Each `ListNode` holds a value of type `i32` and a `next` field which is an `Option` that
/// may contain the next `ListNode` in the list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    /// The value of this node.
    pub val: i32,
    /// The next node in the list.
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    /// Creates a new `ListNode` with the given value.
    ///
    /// # Arguments
    ///
    /// * `val` - The value to be stored in the node.
    ///
    /// # Returns
    ///
    /// * A new `ListNode` with the given value and no next node.
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val,
        }
    }
}

/// `Solution` is a struct that provides a solution to a given problem.
impl Solution {
    /// Doubles the value of each node in the given list. If the doubled value is 10 or more,
    /// it carries the value to the next node.
    ///
    /// # Arguments
    ///
    /// * `head` - The first node of the list.
    ///
    /// # Returns
    ///
    /// * The head of the list after doubling the values.
    pub fn double_it(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head = Some(Box::new(ListNode { val: 0, next: head }));
        let mut prev = head.as_mut().unwrap();
        while let Some(digit) = prev.next.as_mut() {
            let double = digit.val * 2;
            digit.val = double % 10;
            prev.val += double / 10;
            prev = digit;
        }
        if head.as_ref().unwrap().val == 0 {
            head = head.unwrap().next;
        }
        head
    }
}
