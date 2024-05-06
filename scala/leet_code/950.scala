/** This module provides a solution to the problem of revealing a deck in increasing order. The deck is initially sorted
  * in decreasing order, and then revealed by taking the top card and moving the next card to the bottom of the deck.
  * This process is repeated until all cards are revealed in increasing order.
  */
object Solution {

  /** Function to reveal a deck in increasing order.
    *
    * @param deck
    *   an Array[Int] representing the initial deck of cards sorted in decreasing order.
    * @return
    *   an Array[Int] representing the deck revealed in increasing order.
    */
  def deckRevealedIncreasing(deck: Array[Int]): Array[Int] = {

    /** Recursive function to traverse the deck and reveal cards in increasing order.
      *
      * @param dk
      *   a Seq[Int] representing the remaining deck of cards to be revealed.
      * @param acc
      *   an Array[Int] representing the deck revealed so far.
      * @return
      *   an Array[Int] representing the deck revealed in increasing order.
      */
    def traverse(dk: Seq[Int], acc: Array[Int]): Array[Int] = {
      if (dk.isEmpty) acc
      else traverse(dk.tail, dk.head +: acc.last +: acc.init)
    }

    // Sort the deck in reverse order
    val sorted: Array[Int] = deck.sorted.reverse

    // Traverse the sorted deck to reveal cards in increasing order
    traverse(sorted.tail, Array(sorted.head))
  }
}
