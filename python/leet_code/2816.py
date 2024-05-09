"""
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
"""


class ListNode:
    """
    A class to represent a node in a singly linked list.

    Attributes
    ----------
    val : int
        value of the node
    next : ListNode
        reference to the next node in the list

    Methods
    -------
    __init__(self, val=0, next=None)
        Constructs a ListNode with a value and next reference
    """

    def __init__(self, val=0, next=None):
        """
        Constructs a ListNode with a value and next reference.

        Parameters
        ----------
        val : int, optional
            value of the node (default is 0)
        next : ListNode, optional
            reference to the next node in the list (default is None)
        """
        self.val = val
        self.next = next


class Solution(object):
    """
    A class to represent a solution to the problem.

    Methods
    -------
    doubleIt(self, head)
        Doubles the value of each node in the linked list
    """

    def doubleIt(self, head):
        """
        Doubles the value of each node in the linked list.

        Parameters
        ----------
        head : ListNode
            head of the linked list

        Returns
        -------
        ListNode
            head of the modified linked list
        """
        curr = head
        if curr.val > 4:
            head = ListNode(1, head)
        while curr.next:
            curr.val = (curr.val * 2 + (curr.next.val > 4)) % 10
            curr = curr.next
        curr.val = (curr.val * 2) % 10

        return head
