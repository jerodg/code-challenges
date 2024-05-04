/**
 * This class provides a solution for the problem of determining the minimum number of rescue boats required.
 * The problem is solved using a bucket sort approach, where the weight of each person is used as an index into a bucket array.
 * The solution iterates over the bucket array from both ends, pairing the lightest and heaviest people together in the same boat where possible.
 */
class Solution {

    /**
     * Calculates the minimum number of rescue boats required to save all people.
     *
     * @param people An array of integers representing the weight of each person. Each weight is a positive integer.
     * @param limit  The maximum weight that a single boat can carry. It is a positive integer.
     *
     * @return The minimum number of boats required to save all people. It is a positive integer.
     */
    public int numRescueBoats(int[] people, int limit) {
        // Create a bucket array to hold the count of people with each weight
        int[] buckets = new int[limit + 1];

        // Populate the bucket array with the count of people with each weight
        for (int weight : people) {
            buckets[weight]++;
        }

        // Initialize pointers to the start and end of the bucket array
        int start = 0;
        int end = buckets.length - 1;

        // Initialize the count of boats required
        int boats = 0;

        // Iterate over the bucket array from both ends
        while (start <= end) {
            // Move the start pointer to the next non-empty bucket
            while (start <= end && buckets[start] <= 0) start++;
            // Move the end pointer to the previous non-empty bucket
            while (start <= end && buckets[end] <= 0) end--;

            // If both pointers have reached empty buckets, break the loop
            if (buckets[start] <= 0 && buckets[end] <= 0) {
                break;
            }

            // Increment the count of boats required
            boats++;

            // If the sum of the weights at the start and end pointers is less than or equal to the limit,
            // decrement the count at the start pointer, as the person at the start can be paired with the person at the end
            if (start + end <= limit) {
                buckets[start]--;
            }

            // Decrement the count at the end pointer, as the person at the end is always placed in a boat
            buckets[end]--;
        }

        // Return the minimum number of boats required
        return boats;
    }
}
