/// Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
///
/// This program is free software: you can redistribute it and/or modify
/// it under the terms of the Server Side Public License (SSPL) as
/// published by MongoDB, Inc., either version 1 of the
/// License, or (at your option) any later version.
///
/// This program is distributed in the hope that it will be useful,
/// but WITHOUT ANY WARRANTY; without even the implied warranty of
/// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
/// SSPL for more details.
///
/// The above copyright notice and this permission notice shall be included in all
/// copies or substantial portions of the Software.
/// You should have received a copy of the SSPL along with this program.
/// If not, see <https://www.mongodb.com/licensing/server-side-public-license>.

/// A class that represents a node in a singly linked list.
///
/// Each node has an integer value and a reference to the next node in the list.
class ListNode {
  /// The integer value of the node.
  int val;

  /// The next node in the list.
  ListNode? next;

  /// Creates a new node with the given value and next node.
  ///
  /// If no value is provided, the default is 0.
  /// If no next node is provided, the default is null.
  ///
  /// @param val The value of the node.
  /// @param next The next node in the list.
  ListNode([this.val = 0, this.next]);
}

/// A class that provides a solution to a problem.
class Solution {
  /// Removes nodes from a singly linked list.
  ///
  /// This method removes nodes from the list that have a smaller value than the next node.
  /// It starts from the head of the list and iterates through the list, removing nodes as necessary.
  ///
  /// @param head The head of the list.
  /// @return The head of the list after nodes have been removed.
  ListNode? removeNodes(ListNode? head) {
    var node = head;
    var finalAns = head;

    /// A list that stores the nodes of the list.
    List<ListNode?> st = [node];
    node = node?.next;

    while (node != null) {
      while (st.isNotEmpty && st.last!.val < node.val) {
        st.removeLast();
      }

      if (st.isEmpty) {
        finalAns = node;
      } else {
        st.last?.next = node;
      }
      st.add(node);
      node = node.next;
    }
    return finalAns;
  }
}
