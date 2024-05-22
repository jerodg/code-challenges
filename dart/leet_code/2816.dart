/// Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
///
/// This program is free software: you can redistribute it and/or modify it under the terms of the
/// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
/// or (at your option) any later version.
///
/// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
/// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
/// for more details.
///
/// The above copyright notice and this permission notice shall be included in all copies or
/// substantial portions of the Software. You should have received a copy of the SSPL along with this
/// program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
library;

/// A file that defines a linked list node and a solution to double the value of each node in the list.

/// A class that represents a node in a singly linked list.
/// Each node has an integer value and a reference to the next node in the list.
class ListNode {
  /// The integer value of the node.
  int val;

  /// The next node in the list.
  ListNode? next;

  /// Creates a new node with the given value and next node.
  /// If no value is provided, the default is 0.
  /// If no next node is provided, the default is null.
  ListNode([this.val = 0, this.next]);
}

/// A class that provides a solution to double the value of each node in a linked list.
class Solution {
  /// Doubles the value of each node in the given linked list.
  /// If the doubled value is greater than 9, carries the value to the next node.
  /// If the value of the first node is carried, adds a new node with value 1 at the beginning of the list.
  ///
  /// @param head The first node of the linked list.
  /// @return The first node of the modified linked list.
  ListNode? doubleIt(ListNode? head) {
    final firstDigit = dfs(head);

    if (firstDigit == 0) {
      return head;
    }

    return ListNode(1, head);
  }
}

/// Doubles the value of the given node and all following nodes in the list.
/// If the doubled value is greater than 9, carries the value to the next node.
///
/// @param cur The current node to double.
/// @return 1 if the doubled value of the current node is greater than 9, otherwise 0.
int dfs(ListNode? cur) {
  if (cur == null) {
    return 0;
  }

  final newVal = cur.val * 2 + dfs(cur.next);
  cur.val = newVal % 10;

  return newVal > 9 ? 1 : 0;
}
