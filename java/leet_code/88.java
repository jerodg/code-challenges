/**
 * This class provides a solution for the problem of merging two sorted arrays.
 * The problem is solved by first making a copy of the first array, then iterating over the arrays
 * with two pointers, and copying the smaller element at each step back into the first array.
 * After that, if there are remaining elements in either of the arrays, they are copied back into
 * the first array.
 */
class Solution {

    /**
     * Merges two sorted arrays in-place into the first array.
     *
     * @param nums1 The first sorted array. It is an array of integers with a size of m + n, where m
     *              is the number of actual elements.
     * @param m     The number of actual elements in the first array. It is a non-negative integer.
     * @param nums2 The second sorted array. It is an array of integers with a size of n.
     * @param n     The number of actual elements in the second array. It is a non-negative integer.
     */
    public static void merge(final int[] nums1, final int m, final int[] nums2, final int n) {
        // Make a copy of the first array
        final int[] nums1_copy = new int[m];
        System.arraycopy(nums1, 0, nums1_copy, 0, m);

        // Initialize pointers for the first array, the second array, and the copy of the first array
        int p1 = 0;
        int p2 = 0;
        int p = 0;

        // Iterate over the arrays with the pointers
        while (p1 < m && p2 < n) {
            // If the current element in the copy of the first array is smaller than the current
            // element in the second array, copy it back into the first array and move the pointers
            if ((nums1_copy[p1] < nums2[p2])) {
                nums1[p++] = nums1_copy[p1++];
            } else {
                // Otherwise, copy the current element in the second array into the first array and
                // move the pointers
                nums1[p++] = nums2[p2];
                p2++;
            }
        }

        // If there are remaining elements in the copy of the first array, copy them back into the
        // first array
        if (p1 < m) {
            System.arraycopy(nums1_copy, p1, nums1, p1 + p2, m + n - p1 - p2);
        }

        // If there are remaining elements in the second array, copy them into the first array
        if (p2 < n) {
            System.arraycopy(nums2, p2, nums1, p1 + p2, m + n - p1 - p2);
        }
    }
}
