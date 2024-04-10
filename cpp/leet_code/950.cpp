#include <vector>
#include <queue>
#include <algorithm>

// The Solution class contains a method to solve the problem.
class Solution {
public:
  // This method rearranges a deck of cards into a specific order.
  //
  // The deck is sorted in increasing order and then rearranged so that every
  // second card of the sorted deck is placed into the new order.
  //
  // @param deck A reference to a vector of integers representing the deck of cards.
  // @return A vector of integers representing the deck of cards in the new order.
  static std::vector<int> deckRevealedIncreasing(std::vector<int>& deck) {
    // Get the size of the deck.
    auto n = deck.size();

    // Sort the deck in increasing order.
    std::sort(deck.begin(), deck.end());

    // Initialize a queue to hold the indices of the deck.
    std::queue<int> q; // o to n-1

    // Fill the queue with the indices.
    for(int i = 0; i < static_cast<int>(n); i++) {
      q.push(i);
    }

    // Initialize a vector to hold the new order of the deck.
    std::vector<int> ans(n);

    // Rearrange the deck.
    for(size_t i = 0; i < n; i++) {
      // Get the index at the front of the queue.
      int idx = q.front();
      q.pop();

      // Move the front index to the back of the queue.
      q.push(q.front());
      q.pop();

      // Place the card in the new order.
      ans[idx] = deck[i];
    }

    // Return the deck in the new order.
    return ans;
  }
};
