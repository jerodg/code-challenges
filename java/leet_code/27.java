/**
 * This class provides a solution for the problem of removing a specific element from an array.
 * The problem is solved using a two-pointer approach, where one pointer (i) keeps track of the position of the last element that is not equal to the value to be removed,
 * and the other pointer (j) iterates over the array to find the next element that is not equal to the value to be removed.
 * When such an element is found, it is moved to the next position of the last element that is not equal to the value to be removed.
 */
class Solution {

    /**
     * Removes all instances of a specific value from an array in-place and returns the new length of the array.
     *
     * @param nums An array of integers. Each integer can be any valid integer.
     * @param val  The value to be removed from the array. It is an integer.
     *
     * @return The new length of the array after all instances of the value have been removed. It is a non-negative integer.
     */
    public int removeElement(final int[] nums, final int val) {
        // Initialize the first pointer to the first element
        int i = 0;

        // Iterate over the array with the second pointer
        for (int j = 0; j < nums.length; j++) {
            // If the current element is not equal to the value to be removed,
            // move it to the next position of the last element that is not equal to the value to be removed and update the first pointer
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }

        // Return the new length of the array
        return i;
    }
}
