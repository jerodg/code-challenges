/** Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
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

/** Represents a node in a linked list.
  *
  * @constructor
  *   create a new node with a value and the next node.
  * @param _x
  *   the value of the node
  * @param _next
  *   the next node in the list
  *
  * @example
  *   val node1 = new ListNode(1) val node2 = new ListNode(2, node1)
  */
class ListNode(_x: Int = 0, _next: ListNode = null) {
  var next: ListNode = _next
  var x: Int         = _x
}

/** Provides a solution for removing nodes from a linked list.
  */
object Solution {

  /** Removes nodes from a linked list.
    *
    * @param head
    *   the head of the linked list
    * @return
    *   the head of the linked list after removing nodes
    */
  def removeNodes(head: ListNode): ListNode = {

    /** Folds a linked list into a sequence.
      *
      * @param node
      *   the current node
      * @param acc
      *   the accumulated sequence
      * @return
      *   the sequence of node values
      */
    def fold(node: ListNode, acc: Seq[Int] = Seq()): Seq[Int] =
      if (node == null) acc else fold(node.next, node.x +: acc)

    /** Unfolds a sequence into a linked list.
      *
      * @param seq
      *   the sequence of node values
      * @param mx
      *   the maximum node value
      * @param acc
      *   the accumulated linked list
      * @return
      *   the head of the linked list
      */
    def unfold(seq: Seq[Int], mx: Int = 0, acc: ListNode = null): ListNode =
      if (seq.isEmpty) acc
      else if (seq.head < mx) unfold(seq.tail, mx, acc)
      else unfold(seq.tail, seq.head, new ListNode(seq.head, acc))

    unfold(fold(head, Seq()))
  }
}
