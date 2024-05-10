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
 *
 * This file contains a solution for doubling the values of a linked list and calculating the sum.
 * The main class is `Solution` which contains a single public method `doubleIt`.
 */

/**
 * Class representing a node in a singly linked list.
 *
 * @property `val` the value of the node.
 * @property next the next node in the list.
 */
class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

/**
 * Class containing a solution for doubling the values of a linked list and calculating the sum.
 */
class Solution {
    /**
     * This function doubles the values of a linked list and calculates the sum.
     *
     * The function first reverses the linked list. It then iterates over the reversed list, doubling
     * the value of each node and adding it to a running sum. The sum is calculated using a carry
     * mechanism, similar to how addition is performed in elementary arithmetic. The function then
     * reverses the list again to restore its original order and returns the head of the list.
     *
     * @param head the head of the linked list.
     * @return the head of the linked list after doubling the values and calculating the sum.
     */
    fun doubleIt(head: ListNode?): ListNode? {
        var prev = head
        while (head?.next != null) {
            val next = head?.next?.next
            head?.next?.next = prev
            prev = head?.next
            head?.next = next
        }
        var carry = 0
        while (prev != null) {
            val v = carry + prev.`val` * 2
            carry = v / 10
            prev.`val` = v % 10
            if (head == prev) break
            val next = prev.next
            prev.next = head?.next
            head?.next = prev
            prev = next
        }
        return if (carry > 0) ListNode(1)
            .apply { next = head } else head
    }
}
