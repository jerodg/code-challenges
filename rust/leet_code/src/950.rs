use std::collections::VecDeque;

/// `Solution` is a struct that will contain the methods for solving the problem.
struct Solution;

impl Solution {
    /// This function takes a vector of integers as input, sorts it in increasing order,
    /// and then rearranges it in a specific way: it simulates a process of revealing cards
    /// by taking the top card of the deck, revealing it, and then putting the next card to the bottom of the deck.
    ///
    /// # Arguments
    ///
    /// * `deck` - A vector of integers representing the deck of cards.
    ///
    /// # Returns
    ///
    /// * A vector of integers representing the final state of the deck after the revealing process.
    pub fn deck_revealed_increasing(deck: Vec<i32>) -> Vec<i32> {
        // Create a mutable copy of the deck and sort it
        let mut deck = deck;
        deck.sort();

        // Get the number of cards in the deck
        let n = deck.len();

        // Create a queue to simulate the process of revealing cards and putting the next card to the bottom
        let mut q: VecDeque<usize> = (0..n).collect();

        // Initialize the answer vector with zeros
        let mut ans = vec![0; n];

        // Iterate over the sorted deck
        for &card in deck.iter() {
            // Pop the top card from the queue and reveal it
            let i = q.pop_front().unwrap();
            ans[i] = card;

            // If there are still cards in the queue, put the next card to the bottom
            if let Some(j) = q.pop_front() {
                q.push_back(j);
            }
        }

        // Return the final state of the deck
        ans
    }
}
