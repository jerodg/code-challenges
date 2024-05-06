/**
 * Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Server Side Public License (SSPL) as
 * published by MongoDB, Inc., either version 1 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * SSPL for more details.
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * You should have received a copy of the SSPL along with this program.
 * If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * @fileoverview This file contains functions for manipulating linked lists.
 */

/**
 * A class representing a node in a linked list.
 * @class
 * @param {number} val - The value of the node.
 * @param {ListNode} next - The next node in the linked list.
 */
function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * Reverses a linked list.
 * @param {ListNode} node - The head of the linked list.
 * @returns {ListNode} The head of the reversed linked list.
 */
function reverseLinkedList(node) {
    let prev = null;
    let current = node;
    let next = null;

    while (current !== null) {
        next = current.next;
        current.next = prev;
        prev = current;
        current = next;
    }

    node = prev;
    return node;
}

/**
 * Removes nodes from a linked list that are less than the maximum value to its right.
 * @param {ListNode} head - The head of the linked list.
 * @returns {ListNode} The head of the modified linked list.
 */
const removeNodes = function (head) {
    const reversed = reverseLinkedList(head);
    let max = reversed.val;
    let newList = new ListNode(max);
    let current = reversed.next;

    while (current) {
        max = Math.max(max, current.val);
        if (current.val >= max) {
            newList = new ListNode(current.val, newList);
        }
        current = current.next;
    }

    return newList;
};
