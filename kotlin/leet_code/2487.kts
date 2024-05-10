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
 * Represents a node in a singly-linked list.
 * Each node has an integer value and a link to the next node in the list.
 *
 * @property `val` the integer value of this node.
 * @property next the next node in the list.
 */
class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

/**
 * Provides a solution for removing nodes from a singly-linked list.
 */
class Solution {
    /**
     * Removes nodes from a singly-linked list based on certain conditions.
     *
     * The function first converts the linked list into a mutable list for easier manipulation.
     * It then iterates over the list from the end to the beginning, comparing each node with its previous node.
     * If the value of the previous node is greater than or equal to the current node, it adjusts the `next` pointer of the previous node to skip the current node.
     *
     * @param head the head of the linked list.
     * @return the head of the modified linked list.
     */
    fun removeNodes(head: ListNode?): ListNode? {
        val list = mutableListOf<ListNode>()
        var head1 = head

        while (head1 != null) {
            list.add(head1)
            head1 = head1.next
        }

        val n1 = list.size
        var pre = list[n1 - 2]
        var current = list[n1 - 1]

        var n = n1 - 1
        while (n > 0) {
            if (pre.`val` >= current.`val`) {
                pre.next = current
                current = pre
            }
            n--
            if (n - 1 >= 0)
                pre = list[n - 1]
        }
        return current
    }
}
