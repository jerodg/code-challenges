/**
 * @file 2816.cpp
 * @brief Contains the Solution class with a method to double the value of each
 * node in a linked list.
 * @copyright Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
 *
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the Server Side Public License (SSPL) as published by MongoDB,
 * Inc., either version 1 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the SSPL for more details.
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software. You should have received
 * a copy of the SSPL along with this program. If not, see
 * <https://www.mongodb.com/licensing/server-side-public-license>.
 */

#pragma GCC optimize("O3", "unroll-loops")

/**
 * @struct ListNode
 * @brief A node in a singly linked list.
 *
 * Each node contains an integer value and a pointer to the next node in the
 * list.
 */
struct ListNode {
  int val;        // The integer value stored in this node
  ListNode *next; // Pointer to the next node in the list

  // Default constructor initializes the node with a value of 0 and next pointer
  // as nullptr
  ListNode() : val(0), next(nullptr) {}

  // Constructor initializes the node with a given value and next pointer as
  // nullptr
  explicit ListNode(int x) : val(x), next(nullptr) {}

  // Constructor initializes the node with a given value and a given next node
  ListNode(const int x, ListNode *next) : val(x), next(next) {}
};

/**
 * @class Solution
 * @brief Encapsulates the method to solve the problem.
 */
class Solution {
private:
  /**
   * @brief Doubles the value of each node in a linked list.
   *
   * @param head A pointer to the head node of the linked list.
   * @return The carry value after doubling the linked list.
   */
  static int doubledLinkedList(ListNode *head) {
    ListNode *temp = head;
    if (head == nullptr) {
      return 0;
    }
    int carry = doubledLinkedList(head->next);
    const int doubleVal = (temp->val) * 2 + carry;
    const int remainder = doubleVal % 10;
    carry = doubleVal / 10;
    temp->val = remainder;
    return carry;
  }

public:
  /**
   * @brief Doubles the value of each node in a linked list and handles the
   * carry value.
   *
   * @param head A pointer to the head node of the linked list.
   * @return A pointer to the head node of the modified linked list.
   */
  static ListNode *doubleIt(ListNode *head) {
    if (const int final = doubledLinkedList(head); final > 0) {
      const auto newNode = new ListNode(final, nullptr);
      newNode->next = head;
      head = newNode;
    }
    return head;
  }
};
