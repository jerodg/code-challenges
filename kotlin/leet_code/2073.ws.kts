/**
 * This Kotlin module provides a solution for a hypothetical problem where a certain number of tickets need to be bought in a specific order.
 * The solution calculates the minimum time required to buy all the tickets given the constraints.
 *
 * @module leet_code/2073.ws.kts
 */

/**
 * Solution class provides a method to calculate the minimum time required to buy all the tickets.
 */
class Solution {

    /**
     * This function calculates the minimum time required to buy all the tickets.
     *
     * @param tickets An integer array representing the number of tickets that need to be bought in each turn.
     * @param k An integer representing the index of the turn where the buying process starts.
     * @return An integer representing the minimum time required to buy all the tickets.
     *
     * The function iterates over the turns. For each turn, it calculates the minimum time required to buy the tickets in that turn.
     * If the current turn is before or at the starting turn, the time required is the minimum of the number of tickets in the starting turn and the current turn.
     * If the current turn is after the starting turn, the time required is the minimum of one less than the number of tickets in the starting turn and the current turn.
     * The function adds up the time required for all turns and returns the total.
     *
     * Example usage:
     * val solution = Solution()
     * val tickets = intArrayOf(5, 1, 4, 2)
     * val k = 2
     * val timeRequired = solution.timeRequiredToBuy(tickets, k)
     * // timeRequired will be 10 as the minimum time required to buy all the tickets is 10 turns
     */
    fun timeRequiredToBuy(tickets: IntArray, k: Int): Int {
        var ans = 0
        for (i in tickets.indices) {
            ans += if (i <= k) {
                kotlin.math.min(tickets[k], tickets[i])
            } else {
                kotlin.math.min(tickets[k] - 1, tickets[i])
            }
        }
        return ans
    }
}
