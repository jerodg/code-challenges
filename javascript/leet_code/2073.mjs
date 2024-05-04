/**
 * @fileoverview This module provides a function to calculate the time required to buy tickets.
 */
/**
 * Calculates the time required to buy tickets.
 * @param {number[]} tickets - An array where tickets[i] is the number of tickets the ith person wants to buy.
 * @param {number} k - The position of the person in the line.
 * @return {number} - The time required to buy tickets.
 */
var timeRequiredToBuy = function (tickets, k) {
    // Initialize time counter
    let time = 0;
    // Tickets that the person at position k wants to buy
    let kTickets = tickets[k];

    // Loop through each person in the line
    for (let i = 0; i < tickets.length; i++) {
        if (i <= k) {
            // For people ahead of or at k, add the minimum of their ticket count or k's ticket count to time
            time += Math.min(tickets[i], kTickets);
        } else {
            // For people behind k, only consider their ticket count if it's less than k's ticket count
            time += Math.min(tickets[i], kTickets - 1);
        }
    }

    // Return the total time required to buy tickets
    return time;
};
