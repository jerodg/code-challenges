import 'dart:collection';

class Solution {
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
