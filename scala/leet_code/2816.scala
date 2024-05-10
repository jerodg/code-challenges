/** Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
  *
  * This program is free software: you can redistribute it and/or modify it under the terms of the Server Side Public
  * License (SSPL) as published by MongoDB, Inc., either version 1 of the License, or (at your option) any later
  * version.
  *
  * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
  * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL for more details.
  *
  * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
  * Software. You should have received a copy of the SSPL along with this program. If not, see
  * <https://www.mongodb.com/licensing/server-side-public-license>.
  */

/** The `ListNode` class represents a node in a singly linked list. Each node contains an integer value and a reference
  * to the next node in the list.
  *
  * @param _x
  *   The integer value stored in this node. Defaults to 0.
  * @param _next
  *   The next node in the list. Defaults to null.
  */
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next // The next node in the list
  var x: Int         = _x    // The integer value stored in this node
}

/** The `Solution` object contains a method to double the value of each node in a linked list. The new value of each
  * node is the sum of its original value and the value of all nodes that follow it in the list, with the result of this
  * sum being doubled.
  */
object Solution {

  /** This method doubles the value of each node in a linked list. The new value of each node is the sum of its original
    * value and the value of all nodes that follow it in the list, with the result of this sum being doubled.
    *
    * @param head
    *   The head node of the linked list.
    * @return
    *   The head node of the linked list after the values of all nodes have been doubled.
    */
  def doubleIt(head: ListNode): ListNode = {

    /** This helper method calculates the new value for each node in the linked list.
      *
      * @param h
      *   The current node in the linked list.
      * @return
      *   The carry value to be added to the next node in the list.
      */
    def hlpr(h: ListNode): Int = {
      if (h != null) {
        // Calculate the new value for the current node and the carry value for the next node
        val doubledValue = h.x * 2 + hlpr(h.next)
        // Update the value of the current node
        h.x = doubledValue % 10
        // Return the carry value
        doubledValue / 10
      } else 0
    }

    // Double the value of each node in the linked list and handle any remaining carry value
    hlpr(head) match {
      case 0 => head
      case x => new ListNode(x, head)
    }
  }
}
