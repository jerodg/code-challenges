/**
 * @file This module contains a function to calculate the minimum number of rescue boats needed.
 * Each boat carries a maximum weight limit and each person has a weight. The goal is to minimize
 * the number of boats needed to rescue all people.
 */
/**
 * Calculate the minimum number of rescue boats needed.
 *
 * @param {number[]} people - An array of weights of each person.
 * @param {number} limit - The maximum weight that a boat can carry.
 * @returns {number} The minimum number of boats needed to rescue all people.
 *
 * This function works by first counting the number of people with each weight. Then, it iterates
 * from the lightest and heaviest people, trying to pair them in the same boat. If the lightest
 * and heaviest person can't fit in the same boat, the heaviest person takes a boat by themselves.
 * This process continues until all people are accounted for.
 */
function numRescueBoats(people, limit) {
    // Initialize an array to count the number of people with each weight
    var countPerson = new Array(limit).fill(0);
    // Count the number of people with each weight
    for (var i = 0; i < people.length; i++) {
        countPerson[people[i] - 1]++;
    }
    var minIndex = 0; // Index for the lightest person not yet accounted for
    var maxIndex = limit - 2; // Index for the heaviest person not yet accounted for
    var boats = countPerson[limit - 1]; // Number of boats needed, initially count of people with weight equal to limit
    // Iterate until all people are accounted for
    while (minIndex <= maxIndex) {
        // Find the next lightest person not yet accounted for
        while (countPerson[minIndex] === 0 && minIndex <= maxIndex) {
            minIndex++;
        }
        // Find the next heaviest person not yet accounted for
        while (countPerson[maxIndex] === 0 && minIndex <= maxIndex) {
            maxIndex--;
        }
        // If the lightest and heaviest person can fit in the same boat, pair them
        if (minIndex < maxIndex) {
            if ((minIndex + 1) + (maxIndex + 1) <= limit) {
                countPerson[minIndex]--;
            }
            boats++;
            countPerson[maxIndex]--;
        }
        else if (minIndex === maxIndex) {
            // If the lightest and heaviest person are the same, they take a boat by themselves
            if (maxIndex + 1 > limit / 2) {
                boats += countPerson[maxIndex];
            }
            else {
                boats += Math.ceil(countPerson[maxIndex] / 2);
            }
            maxIndex = -1;
            minIndex = limit;
        }
    }
    // Return the minimum number of boats needed
    return boats;
}
