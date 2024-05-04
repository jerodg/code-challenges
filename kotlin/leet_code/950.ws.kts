/**
 * This Kotlin module provides a solution for the LeetCode problem 950. Reveal Cards In Increasing Order.
 * The solution reveals cards in increasing order from a deck of cards sorted in decreasing order.
 *
 * @module leet_code/950.ws.kts
 */

import java.util.*

/**
 * Solution class provides a method to reveal cards in increasing order.
 */
class Solution {

    /**
     * This function reveals cards in increasing order from a deck of cards sorted in decreasing order.
     *
     * @param deck An integer array representing the deck of cards sorted in decreasing order.
     * @return An integer array representing the order in which the cards are revealed.
     *
     * The function sorts the deck of cards in increasing order. It then uses a recursive function to simulate the process of revealing cards.
     * The recursive function takes the deck of cards, the result array, the current index in the deck, the current index in the result, and a boolean indicating whether to skip the current card.
     * It iterates over the cards in the deck. If the current card should not be skipped, it places the card in the result array and moves to the next card in the deck.
     * If the current card should be skipped, it moves to the next card in the result array without changing the deck.
     * The function continues this process until all cards in the deck have been placed in the result array.
     *
     * Example usage:
     * val solution = Solution()
     * val deck = intArrayOf(17,13,11,2,3,5,7)
     * val revealedOrder = solution.deckRevealedIncreasing(deck)
     * // revealedOrder will be [2,13,3,11,5,17,7]
     */
    fun deckRevealedIncreasing(deck: IntArray): IntArray {
        val N = deck.size
        val result = IntArray(N)

        Arrays.sort(deck)

        return everyOther(deck, result, 0, 0, false)
    }

    /**
     * This recursive function simulates the process of revealing cards.
     *
     * @param deck An integer array representing the deck of cards sorted in increasing order.
     * @param result An integer array representing the order in which the cards are revealed.
     * @param indexInDeck The current index in the deck.
     * @param indexInResult The current index in the result.
     * @param skip A boolean indicating whether to skip the current card.
     * @return An integer array representing the order in which the cards are revealed.
     *
     * The function iterates over the cards in the deck. If the current card should not be skipped, it places the card in the result array and moves to the next card in the deck.
     * If the current card should be skipped, it moves to the next card in the result array without changing the deck.
     * The function continues this process until all cards in the deck have been placed in the result array.
     */
    private tailrec fun everyOther(
        deck: IntArray,
        result: IntArray,
        indexInDeck: Int,
        indexInResult: Int,
        skip: Boolean
    ): IntArray {
        val N = deck.size

        if (indexInDeck == N) {
            return result
        }

        var newIndexInDeck = indexInDeck
        var newIndexInResult = indexInResult
        var newSkip = skip

        while (newIndexInResult < N) {
            if (result[newIndexInResult] == 0) {
                if (!newSkip) {
                    result[newIndexInResult] = deck[newIndexInDeck]
                    newIndexInDeck++
                }
                newSkip = !newSkip
            }
            newIndexInResult++
        }

        return everyOther(deck, result, newIndexInDeck, 0, newSkip)
    }
}
