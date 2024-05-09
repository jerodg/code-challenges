/*
Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
*/

/// <summary>
/// Represents a node in a linked list.
/// </summary>
public class ListNode {
    /// <summary>
    /// The value of the node.
    /// </summary>
    public int val;
    /// <summary>
    /// The next node in the linked list.
    /// </summary>
    public ListNode next;
    /// <summary>
    /// Initializes a new instance of the ListNode class.
    /// </summary>
    /// <param name="val">The value of the node.</param>
    /// <param name="next">The next node in the linked list.</param>
    public ListNode(int val=0, ListNode next=null) {
        this.val = val;
        this.next = next;
    }
}

/// <summary>
/// Provides a solution for doubling the value of each node in a linked list.
/// </summary>
public class Solution {
    /// <summary>
    /// Doubles the value of each node in the linked list.
    /// </summary>
    /// <param name="head">The head of the linked list.</param>
    /// <returns>A new linked list with each node's value doubled.</returns>
    public ListNode DoubleIt(ListNode head) {
        ListNode first = new ListNode(0, head), prev = first;
        while(head!=null) {
            int d = head.val * 2;
            if (d>=10) prev.val++;
            head.val = d%10;
            prev = head;
            head = head.next;
        }
        return first.val > 0 ? first : first.next;
    }
}
