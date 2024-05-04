// Package leet_code provides solutions for LeetCode problems.
//
// This file provides a solution for the problem of revealing cards in increasing order.
// The deck is sorted in increasing order, and the deck is revealed by taking the top card of the deck and revealing it, then taking the next card of the deck and moving it to the bottom, repeating until all cards are revealed.
package leet_code

import "sort"

// deckRevealedIncreasing reveals the cards in increasing order.
//
// It accepts one parameter:
// - deck: a slice of integers representing the deck of cards.
//
// The function returns a slice of integers representing the order in which the cards are revealed.
//
// The function first sorts the deck in increasing order. It then simulates the process of revealing the cards by using a queue to keep track of the indices of the cards.
// For each card in the sorted deck, it assigns the card to the position indicated by the first index in the queue, then removes the first index from the queue.
// If there are still indices left in the queue, it moves the first index to the end of the queue.
//
// Time complexity analysis:
// - Best-case: O(n log n), due to the sorting of the deck.
// - Worst-case: O(n log n), due to the sorting of the deck.
// - Average-case: O(n log n), due to the sorting of the deck.
func deckRevealedIncreasing(deck []int) []int {
	// q is a queue that keeps track of the indices of the cards.
	var q []int
	for i := 0; i < len(deck); i++ {
		q = append(q, i)
	}
	// Sort the deck in increasing order.
	sort.Ints(deck)
	// ans is the order in which the cards are revealed.
	ans := make([]int, len(deck))
	for _, card := range deck {
		// Assign the card to the position indicated by the first index in the queue.
		ans[q[0]] = card
		// Remove the first index from the queue.
		q = q[1:]
		// If there are still indices left in the queue, move the first index to the end of the queue.
		if len(q) > 0 {
			q = append(q, q[0])
			q = q[1:]
		}
	}
	// Return the order in which the cards are revealed.
	return ans
}
