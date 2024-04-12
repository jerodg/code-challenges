/**
 * Function to rearrange a deck of cards into a specific order.
 *
 * Given a deck of cards (represented as an array of numbers), the function rearranges the deck into a specific order.
 * The deck is sorted in increasing order, and then the following steps are repeated until the deck is empty:
 * - If the result array is not empty, the last card in the result array is moved to the front.
 * - The last card in the deck is moved to the front of the result array.
 *
 * @param {number[]} deck - The deck of cards to be rearranged, represented as an array of numbers.
 * @returns {number[]} The rearranged deck of cards.
 */
function deckRevealedIncreasing(deck) {
    var result = [];
    deck.sort(function (a, b) { return a - b; });
    while (deck.length) {
        if (result.length)
            result.unshift(result.pop());
        result.unshift(deck.pop());
    }
    return result;
}
