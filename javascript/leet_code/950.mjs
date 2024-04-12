/**
 * This function takes an array of numbers (deck) as input and returns a new array
 * where the numbers are arranged in a specific order. The order is determined by
 * the following steps:
 * 1. Sort the input array in descending order.
 * 2. Initialize an empty array (response).
 * 3. While the input array is not empty:
 *    - If the response array has more than one element, move the last element to the front.
 *    - Add the first element of the input array to the front of the response array.
 *    - Remove the first element from the input array.
 * 4. Return the response array.
 *
 * @param {number[]} deck - The input array of numbers.
 * @return {number[]} - The output array of numbers arranged in the specified order.
 */
let deckRevealedIncreasing = function (deck) {
    // Sort the input array in descending order.
    deck.sort((a, b) => b - a);

    // Initialize an empty array.
    let response = [];

    // While the input array is not empty:
    while (deck.length > 0) {
        // If the response array has more than one element, move the last element to the front.
        if (response.length > 1) {
            response.unshift(response.pop());
        }
        // Add the first element of the input array to the front of the response array.
        response.unshift(deck[0]);
        // Remove the first element from the input array.
        deck.shift();
    }
    // Return the response array.
    return response;
};
