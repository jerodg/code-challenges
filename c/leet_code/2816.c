/**
 * @file leet_code/2816.c
 * @brief This file contains the implementation of functions to double the value of a linked list interpreted as a binary number.
 *
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
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
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */

#pragma GCC optimize("O3,unroll-loops")
#include <stdlib.h>

/**
 * @brief A struct representing a node in a singly-linked list.
 */
struct ListNode {
    int val;               /**< The value of the node. */
    struct ListNode* next; /**< A pointer to the next node in the list. */
};

/**
 * @brief A helper function that doubles the value of a linked list interpreted as a binary number.
 *
 * @param node A pointer to the current node in the list.
 * @return int The carry from the doubling operation.
 */
int helper(struct ListNode* node) {
    int num = 0;
    if (node->next == NULL) {
        num = node->val * 2;
    } else {
        num = node->val * 2 + helper(node->next);
    }
    node->val = num % 10;
    return num / 10;
}

/**
 * @brief Doubles the value of a linked list interpreted as a binary number.
 *
 * @param head A pointer to the head of the list.
 * @return struct ListNode* A pointer to the head of the list after doubling.
 */
struct ListNode* doubleIt(struct ListNode* head) {
    int num = helper(head);
    if (num > 0) {
        struct ListNode* newHead = (struct ListNode*)malloc(sizeof(struct ListNode));
        newHead->val = num;
        newHead->next = head;
        return newHead;
    } else {
        return head;
    }
}
