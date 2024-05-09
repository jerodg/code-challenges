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

from typing import Optional


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


class Solution:
    """
    A class to represent a solution to the problem.

    Methods
    -------
    removeNodes(self, head)
        Removes nodes from the linked list based on certain conditions
    """

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Removes nodes from the linked list based on certain conditions.

        The function first reverses the linked list. Then it iterates over the reversed list and creates a new list.
        While creating the new list, it only includes nodes whose value is greater than or equal to the maximum value seen so far.

        Parameters
        ----------
        head : Optional[ListNode]
            head of the linked list

        Returns
        -------
        Optional[ListNode]
            head of the modified linked list
        """
        dummy = head
        rev = None

        # reverse the list and store in temp rev
        while dummy:
            next_node = dummy.next
            dummy.next = rev
            rev = dummy
            dummy = next_node

        # iterate over reversed list
        dummy = rev
        head = None
        max_value = float('-inf')

        # Create new list
        while dummy:
            if dummy.val >= max_value:
                max_value = dummy.val

                # same logic as for reversing
                new_node = dummy.next
                dummy.next = head
                head = dummy
                dummy = new_node
            else:
                dummy = dummy.next

        return head
