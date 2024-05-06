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
 * Represents a ListNode.
 * @property {number} val - The value of the node.
 * @property {ListNode | null} next - The next node in the list.
 */
class ListNode {
    val: number
    next: ListNode | null

    /**
     * @param {number} val - The value of the node.
     * @param {ListNode | null} next - The next node in the list.
     */
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.next = (next === undefined ? null : next)
    }
}

/**
 * Reverses a linked list.
 * @param {ListNode | null} head - The head of the list to reverse.
 * @returns {ListNode | null} - The head of the reversed list.
 */
function reverseList(head: ListNode | null): ListNode | null {
    let prev = null, cur = head;
    while (cur !== null) {
        let next = cur.next;
        cur.next = prev;
        prev = cur;
        cur = next;
    }
    return prev;
}

/**
 * Removes nodes from a linked list that have a greater value than the next node.
 * @param {ListNode | null} head - The head of the list to modify.
 * @returns {ListNode | null} - The head of the modified list.
 */
function removeNodes(head: ListNode | null): ListNode | null {
    head = reverseList(head);
    let cur = head;
    while (cur !== null && cur.next !== null) {
        if (cur.val > cur.next.val) {
            cur.next = cur.next.next;
        } else {
            cur = cur.next;
        }
    }
    return reverseList(head);
}
