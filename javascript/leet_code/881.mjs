/**
 * @file This module is responsible for calculating the minimum number of rescue boats required to
 * save people.
 * Each boat carries a weight limit, and each person has a weight. The goal is to minimize the
 * number of boats needed.
 * The solution uses a two-pointer technique to pair the heaviest and lightest person until all
 * people are accounted for.
 * @module leet_code/881
 */

/**
 * Calculates the minimum number of rescue boats required.
 *
 * The function sorts the array of people's weights in ascending order. Then, it uses a two-pointer
 * technique to pair the heaviest person (right pointer) with the lightest person (left pointer) if
 * possible. If the sum of their weights is less than or equal to the limit, they can share a boat,
 * and the left pointer moves to the next person. If not, the heaviest person takes a boat alone,
 * and the right pointer moves to the next person. This process continues until all people are
 * accounted for.
 *
 * @param {number[]} people - An array of integers where each integer represents the weight of a person.
 * @param {number} limit - The maximum weight that a rescue boat can carry.
 * @returns {number} The minimum number of rescue boats required.
 */
const numRescueBoats = function (people, limit) {
    // Initialize the result to 0
    let result = 0;
    // Initialize two pointers, left and right
    let l = 0, r = people.length - 1;
    // Sort the array of people's weights in ascending order
    people.sort((a, b) => a - b);
    // Continue until all people are accounted for
    while (l <= r) {
        // If the lightest and heaviest person can share a boat
        if (people[l] + people[r] <= limit) {
            // Increment the result
            result++;
            // Move the left pointer to the next person
            l++;
        }
        // If the heaviest person needs to take a boat alone
        else if (people[r] <= limit || l === r && people[l] <= limit) {
            // Increment the result
            result++;
        }
        // Move the right pointer to the next person
        r--;
    }
    // Return the minimum number of rescue boats required
    return result;
};
