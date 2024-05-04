/**
 * @fileoverview This module contains a solution for a problem where you need to calculate the time required to buy a
 *     specific ticket. The problem is solved by using a while loop to simulate the process of buying tickets.
 */

/**
 * Function to calculate the time required to buy a specific ticket.
 * The function iterates over the tickets array and uses a while loop to simulate the process of buying tickets.
 * It calculates the time required to buy the kth ticket.
 *
 * @param {number[]} tickets - The tickets available, represented as an array of numbers where each number represents
 *     the time required to buy the ticket.
 * @param {number} k - The index of the ticket to buy.
 * @returns {number} The time required to buy the kth ticket.
 */
function timeRequiredToBuy(tickets: number[], k: number): number {
    // Initialize the total time required and the number of tickets needed to buy
    let seconds: number = 0;
    let ticketNeedToBuy: number = tickets[k];
    // Calculate the number of tickets that can be bought faster than the kth ticket
    let gap: number = tickets.filter((item, index) => index < k && item < tickets[k]).length;

    // While there are tickets needed to buy
    while (ticketNeedToBuy > 1) {
        // Add the total number of tickets to the total time required
        seconds += tickets.length;

        // Update the tickets array by reducing the time required to buy each ticket by 1 and removing the tickets that
        // have been bought
        tickets = tickets.reduce((newArr: number[], currentValue, currentIndex) => {
            if (--currentValue !== 0) {
                newArr.push(currentValue);
            }
            return newArr;
        }, []);

        // Decrement the number of tickets needed to buy
        ticketNeedToBuy--;
    }
    // Return the total time required plus the time required to buy the kth ticket
    return seconds + k - gap + 1;
}
