/**
 * @file 2487.c
 * @brief This module provides functions to manipulate a linked list.
 *
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

#pragma GCC optimize("O3,unroll-loops")

#include <stddef.h>

/**
 * @struct ListNode
 * @brief A node in a singly linked list.
 */
struct ListNode {
    int val;               /**< The value of the node */
    struct ListNode* next; /**< Pointer to the next node */
};

/**
 * @brief Reverses a linked list.
 * @param head The head of the list to reverse.
 * @return The new head of the reversed list.
 *
 * This function iterates over the linked list, reversing the links between nodes.
 * It uses a temporary variable to hold the next node before changing the link direction.
 */
struct ListNode* reverse(struct ListNode* head) {
    struct ListNode *current = NULL, *temp = head;
    while (temp != NULL) {
        struct ListNode* tempnext = temp->next;
        temp->next = current;
        current = temp;
        temp = tempnext;
    }
    head = current;
    return head;
}

/**
 * @brief Removes nodes from a linked list based on certain criteria.
 * @param head The head of the list from which to remove nodes.
 * @return The head of the list after removals.
 *
 * This function first reverses the linked list, then iterates over the reversed list.
 * It removes nodes based on a certain criteria and then reverses the list again before returning it.
 */
struct ListNode* removeNodes(struct ListNode* head) {
    head = reverse(head);
    int mock = 0;
    struct ListNode *temp = head, *current = head;
    while (temp != NULL) {
        if (mock <= temp->val) {
            mock = temp->val;
            current = temp;
        } else {
            current->next = temp->next;
        }
        temp = temp->next;
    }
    head = reverse(head);
    return head;
}
