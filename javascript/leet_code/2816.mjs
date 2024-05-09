/**
 * Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * ListNode is a class that represents a node in a singly linked list.
 * Each node contains a value and a reference to the next node in the list.
 *
 * @property {*} val - The value stored in the node.
 * @property {ListNode} next - The next node in the list.
 */
function ListNode(val, next) {
    // The value stored in the node. If no value is provided, defaults to 0.
    this.val = val === undefined ? 0 : val;
    // The next node in the list. If no next node is provided, defaults to null.
    this.next = next === undefined ? null : next;
}

/**
 * This function takes a linked list of numbers and doubles each number in the list.
 * If a number in the list is greater than 4, it adds a new node with the value 0 at the beginning of the list.
 * The function modifies the original list and returns the modified list.
 *
 * @param {ListNode} head - The head node of the linked list.
 * @returns {ListNode} The head node of the modified linked list.
 */
const doubleIt = function (head) {
    // If the value of the head node is greater than 4, add a new node with the value 0 at the beginning of the list
    if (head.val > 4) {
        head = new ListNode(0, head);
    }
    // Start at the head node
    let curr = head;

    // Traverse the list
    while (curr !== null) {
        // Double the value of the current node and take the remainder when divided by 10
        curr.val = curr.val * 2 % 10;
        // If the next node exists and its value is greater than 4, increment the value of the current node
        if (curr.next !== null && curr.next.val > 4) {
            curr.val += 1;
        }
        // Move to the next node
        curr = curr.next;
    }
    // Return the head node of the modified list
    return head;
};
