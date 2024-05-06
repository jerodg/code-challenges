/**
 * Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
 * <p>
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Server Side Public License (SSPL) as
 * published by MongoDB, Inc., either version 1 of the
 * License, or (at your option) any later version.
 * <p>
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * SSPL for more details.
 * <p>
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * You should have received a copy of the SSPL along with this program.
 * If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * This class represents a node in a singly linked list.
 * Each node contains an integer value and a reference to the next node in the list.
 */
public class ListNode {
    /**
     * The integer value stored in this node.
     */
    int val = 0;

    /**
     * The next node in the list.
     */
    ListNode next = null;

    /**
     * Default constructor. Creates a new node with a value of 0 and no next node.
     */
    ListNode() {
    }

    /**
     * Creates a new node with the given value and no next node.
     *
     * @param val The integer value to store in the node.
     */
    ListNode(final int val) {
        this.val = val;
    }

    /**
     * Creates a new node with the given value and next node.
     *
     * @param val The integer value to store in the node.
     * @param next The next node in the list.
     */
    ListNode(final int val, final ListNode next) {
        this.val = val;
        this.next = next;
    }
}

/**
 * This class provides a solution for removing nodes from a singly linked list.
 */
class Solution {
    /**
     * Removes nodes from a singly linked list.
     * The removal process is done in two steps:
     * 1. Reverse the list.
     * 2. Remove nodes that have a smaller value than the previous node.
     *
     * @param head The head of the list.
     * @return The head of the list after removal.
     */
    public static ListNode removeNodes(final ListNode head) {
        if (head.next == null) {
            return head;
        }
        ListNode prevNode = head;
        ListNode currentNode = head.next;

        // Reverse the list
        while (currentNode != null) {
            final ListNode nextNode = currentNode.next;
            currentNode.next = prevNode;
            prevNode = currentNode;
            currentNode = nextNode;
        }
        head.next = null;
        ListNode node = prevNode;

        // Remove nodes that have a smaller value than the previous node
        currentNode = node.next;
        while (currentNode != null) {
            if (currentNode.val < prevNode.val) {
                currentNode = currentNode.next;
            } else {
                final ListNode nextNode = currentNode.next;
                currentNode.next = prevNode;
                prevNode = currentNode;
                currentNode = nextNode;
            }
        }
        node.next = null;
        node = prevNode;
        return node;
    }
}
