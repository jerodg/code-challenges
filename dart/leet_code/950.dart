/// Dart implementation of the LeetCode problem 950: Reveal Cards In Increasing Order.
///
/// This module contains a class `Solution` with a method `deckRevealedIncreasing`.
/// The `deckRevealedIncreasing` method takes in one parameter:
/// - `deck`: A list of integers representing the deck of cards.
///
/// The method returns a list of integers representing the order of revealing the cards.
/// The deck is revealed in the following way: take the top card of the deck, show it, and put it on the table.
/// Then, take the next card of the deck, put it at the bottom of the deck, and continue until all cards are revealed.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `deck` is a list of integers.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.

import 'dart:collection';

class Solution {
  /// Reveals the cards in increasing order.
  ///
  /// This method uses a queue to simulate the process of revealing the cards.
  /// It sorts the deck in ascending order and then iterates over the deck from the last card to the first card.
  /// For each card, if the queue is not empty, it moves the first card in the queue to the end of the queue.
  /// Then, it adds the current card to the queue.
  /// Finally, it returns the order of revealing the cards.
  ///
  /// @param deck A list of integers representing the deck of cards.
  /// @return A list of integers representing the order of revealing the cards.
  List<int> deckRevealedIncreasing(List<int> deck) {
    deck.sort();
    Queue<int> dq = Queue<int>();
    for (int i = deck.length - 1; i >= 0; i--) {
      if (dq.isNotEmpty) {
        dq.add(dq.removeFirst());
      }
      dq.add(deck[i]);
    }
    return dq.toList();
  }
}
