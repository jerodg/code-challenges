/**
 * This class provides a solution for the problem of removing duplicates from a sorted array.
 * The problem is solved using a two-pointer approach, where one pointer (i) keeps track of the position of the last unique element,
 * and the other pointer (j) iterates over the array to find the next unique element.
 * When a unique element is found, it is moved to the next position of the last unique element.
 */
class Solution {

    /**
     * Removes duplicates from a sorted array in-place and returns the new length of the array.
     *
     * @param nums An array of integers sorted in non-decreasing order. Each integer can be any valid integer.
     *
     * @return The new length of the array after duplicates have been removed. It is a non-negative integer.
     */
    public int removeDuplicates(final int[] nums) {
        // If the array is empty, return 0
        if (0 == nums.length) {
            return 0;
        }

        // Initialize the first pointer to the first element
        int i = 0;

        // Iterate over the array with the second pointer
        for (int j = 1; j < nums.length; j++) {
            // If the current element is not equal to the last unique element,
            // move it to the next position of the last unique element and update the first pointer
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }

        // Return the new length of the array
        return i + 1;
    }
}
