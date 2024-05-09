/**
 * Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
 * <p>
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 * <p>
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 * <p>
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * ListNode is a class that represents a node in a singly linked list.
 * Each node contains an integer value and a reference to the next node in the list.
 */
public class ListNode {
    int val = 0; // The value stored in this node.
    ListNode next = null; // The next node in the list.

    /**
     * Default constructor. Initializes the node with a value of 0 and no next node.
     */
    ListNode() {
        super();
    }

    /**
     * Constructor that initializes the node with a given value and no next node.
     *
     * @param val The value to be stored in the node.
     */
    ListNode(int val) {
        super();
        this.val = val;
    }

    /**
     * Constructor that initializes the node with a given value and a reference to the next node.
     *
     * @param val The value to be stored in the node.
     * @param next The next node in the list.
     */
    ListNode(final int val, final ListNode next) {
        super();
        this.val = val;
        this.next = next;
    }
}

/**
 * Solution class contains methods to solve the problem.
 */
class Solution {
    /**
     * This method doubles the value of each node in the linked list.
     * If the doubled value is greater than 9, it carries the value to the previous node.
     *
     * @param head The head node of the linked list.
     * @return The head of the modified linked list.
     */
    public static ListNode doubleIt(final ListNode head) {
        final ListNode newHead = new ListNode(0, head); // Create a new head node.
        ListNode preNode = newHead; // Initialize the previous node as the new head node.
        ListNode curNode = head; // Initialize the current node as the head node.
        int c = 0, t = 0; // Initialize the carry and temporary variables.
        while (curNode != null) {
            t = curNode.val << 1; // Double the value of the current node.
            c = t / 10; // Calculate the carry.
            preNode.val += c; // Add the carry to the value of the previous node.
            curNode.val = t - c * 10; // Update the value of the current node.
            preNode = curNode; // Move the previous node to the current node.
            curNode = curNode.next; // Move to the next node.
        }
        return newHead.val > 0 ? newHead : head; // Return the new head if its value is greater than 0, otherwise return the original head.
    }
}
