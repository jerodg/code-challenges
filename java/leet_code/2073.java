/**
 * This class provides a solution for the problem of calculating the time required to buy a certain number of tickets.
 * The problem is solved by iterating over the array of tickets and adding the minimum of the kth ticket and the current ticket to the total time.
 * If the current ticket index is greater than k, the kth ticket minus one is considered instead.
 *
 * @author jerodg
 */
class Solution {

    /**
     * Calculates the time required to buy a certain number of tickets.
     *
     * @param tickets An array of integers representing the time required to buy each ticket. Each integer can be any valid integer.
     * @param k       The index of the ticket to be bought. It is a non-negative integer.
     *
     * @return The total time required to buy the tickets. It is a non-negative integer.
     */
    public int timeRequiredToBuy(final int[] tickets, final int k) {
        // Initialize the total time to 0
        int ans = 0;

        // Iterate over the array of tickets
        for (int i = 0; i < tickets.length; i++) {
            // If the current ticket index is less than or equal to k,
            // add the minimum of the kth ticket and the current ticket to the total time
            if (i <= k) {
                ans += Math.min(tickets[k], tickets[i]);
            } else {
                // Otherwise, add the minimum of the kth ticket minus one and the current ticket to the total time
                ans += Math.min(tickets[k] - 1, tickets[i]);
            }
        }

        // Return the total time
        return ans;
    }
}
