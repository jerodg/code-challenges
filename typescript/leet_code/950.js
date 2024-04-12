/**
 * @fileoverview This module contains a solution for the "Reveal Cards In Increasing Order" problem from LeetCode.
 * The problem is solved by using a deque to simulate the process of revealing cards.
 */
/**
 * Function to rearrange a deck of cards into a specific order.
 * Given a deck of cards (represented as an array of numbers), the function rearranges the deck into a specific order.
 * The deck is sorted in increasing order, and then the following steps are repeated until the deck is empty:
 * - If the result array is not empty, the last card in the result array is moved to the front.
 * - The last card in the deck is moved to the front of the result array.
 *
 * @param {number[]} deck - The deck of cards to be rearranged, represented as an array of numbers.
 * @returns {number[]} The rearranged deck of cards.
 */
function deckRevealedIncreasing(deck) {
    // Initialize the result array
    var result = [];
    // Sort the deck in increasing order
    deck.sort(function (a, b) { return a - b; });
    // While the deck is not empty
    while (deck.length) {
        // If the result array is not empty, move the last card in the result array to the front
        if (result.length)
            result.unshift(result.pop());
        // Move the last card in the deck to the front of the result array
        result.unshift(deck.pop());
    }
    // Return the rearranged deck of cards
    return result;
}
