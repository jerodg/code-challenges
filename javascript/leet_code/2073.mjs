/**
 * @param {number[]} tickets
 * @param {number} k
 * @return {number}
 */
var timeRequiredToBuy = function (tickets, k) {
    let time = 0; // Initialize time counter
    let kTickets = tickets[k]; // Tickets that the person at position k wants to buy

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

    return time;
};
