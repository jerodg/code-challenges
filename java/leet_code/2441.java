/**
 * This module is part of a leet code solution. It contains a single class, Solution, which
 * provides a method to find the maximum positive integer that also exists as a negative integer in the array.
 * The method uses an array as a hashmap to solve the problem.
 */
class Solution {

    /**
     * This method finds the maximum positive integer that also exists as a negative integer in the array.
     *
     * @param nums The input array. It is expected to be a non-null integer array.
     *
     * @return The maximum positive integer that also exists as a negative integer in the array.
     * If no such integer exists, it returns -1. The return type is an integer.
     */
    public static int findMaxK(final int[] nums) {
        // An array used as a hashmap to store the negative integers from the input array
        final int[] hm = new int[1001];
        // Variable to store the maximum positive integer that also exists as a negative integer in the array
        int max = -1;

        // Iterate over the input array
        for (final int n : nums) {
            // If the current integer is negative, store it in the hashmap
            if (n < 0) {
                hm[-n] = n;
            }
        }

        // Iterate over the input array again
        for (final int n : nums) {
            // If the current integer is positive and it also exists as a negative integer in the array,
            // update the max variable
            if (n > 0 && hm[n] != 0) {
                max = Math.max(max, n);
            }
        }
        // Return the maximum positive integer that also exists as a negative integer in the array
        return max;
    }
}
