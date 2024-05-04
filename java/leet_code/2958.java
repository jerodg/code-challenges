import java.util.HashMap;

/**
 * This class provides a solution for the problem of finding the maximum length of a subarray with at most K distinct elements.
 * The problem is solved using a sliding window approach, where a window is maintained between two pointers (left and right).
 * A HashMap is used to keep track of the count of each element in the window.
 * If the count of an element exceeds K, the left pointer is moved to the right until the count becomes K.
 * The maximum length of the window is updated at each step.
 */
class Solution {

    /**
     * Finds the maximum length of a subarray with at most K distinct elements.
     *
     * @param nums An array of integers. Each integer can be any valid integer.
     * @param k    The maximum number of distinct elements allowed in the subarray. It is a non-negative integer.
     *
     * @return The maximum length of a subarray with at most K distinct elements. It is a non-negative integer.
     */
    public static int maxSubarrayLength(final int[] nums, final int k) {
        // Initialize the left pointer to the first element
        int left = 0;

        // Initialize a HashMap to keep track of the count of each element in the window
        final HashMap<Integer, Integer> counter = new HashMap<>();

        // Initialize the maximum length of the window
        int max_length = 0;

        // Iterate over the array with the right pointer
        for (int right = 0; right < nums.length; right++) {
            // Increase the count of the current element in the HashMap
            counter.put(nums[right], counter.getOrDefault(nums[right], 0) + 1);

            // If the count of the current element exceeds K, move the left pointer to the right until the count becomes K
            while (counter.get(nums[right]) > k) {
                counter.put(nums[left], counter.get(nums[left]) - 1);
                if (0 == counter.get(nums[left])) {
                    counter.remove(nums[left]);
                }
                left++;
            }

            // Update the maximum length of the window
            max_length = Math.max(max_length, right - left + 1);
        }

        // Return the maximum length of the window
        return max_length;
    }
}
