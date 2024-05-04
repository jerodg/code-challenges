/**
 * This Kotlin module provides a solution for the LeetCode problem 881. Boats to Save People.
 * The solution calculates the minimum number of boats required to rescue all people, given a weight limit for each boat.
 *
 * @module leet_code/881.ws.kts
 */

/**
 * Solution class provides methods to calculate the minimum number of boats required to rescue all people.
 */
class Solution {

    /**
     * This function calculates the minimum number of boats required to rescue all people.
     *
     * @param people An integer array representing the weights of each person.
     * @param limit An integer representing the maximum weight that each boat can carry.
     * @return The minimum number of boats required to rescue all people.
     *
     * The function sorts the array of people's weights in ascending order. It then uses a two-pointer approach,
     * with one pointer starting from the beginning of the array (lightest person) and the other from the end (heaviest person).
     * If the sum of the weights of the two people is less than or equal to the limit, they can share a boat and both pointers move.
     * If not, the heavier person takes a boat alone and only the pointer at the end moves.
     * The function continues this process until all people have been assigned to a boat.
     *
     * Example usage:
     * val solution = Solution()
     * val people = intArrayOf(1, 2)
     * val limit = 3
     * val numBoats = solution.numRescueBoats(people, limit)
     * // numBoats will be 1 as both people can share a boat
     */
    fun numRescueBoats(people: IntArray, limit: Int): Int {
        // Initialize the number of boats required
        var antokir: Int = 0
        // Sort the array of people's weights
        people.sort()
        // Initialize two pointers, one at the start and one at the end of the array
        var l: Int = 0
        var r: Int = people.size - 1
        // Continue until all people have been assigned to a boat
        while (l <= r) {
            // If the sum of the weights of the two people is less than or equal to the limit, they can share a boat
            if (people[r] + people[l] <= limit) {
                l++
                r--
                antokir++
            }
            // If not, the heavier person takes a boat alone
            else if (people[r] <= limit) {
                r--
                antokir++
            }
        }
        // Return the minimum number of boats required
        return antokir;
    }
}
