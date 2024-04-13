/**
 * Function to merge two sorted arrays in-place
 *
 * @param {number[]} nums1 - The first sorted array
 * @param {number} m - The number of initialized elements in nums1
 * @param {number[]} nums2 - The second sorted array
 * @param {number} n - The number of initialized elements in nums2
 * @returns {void} - The function does not return anything, it modifies nums1 in-place
 */
const merge = function (nums1, m, nums2, n) {
    // Initialize pointers for nums1, nums2 and the merged array
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;

    // While there are elements in both arrays
    while (0 <= i && 0 <= j) {
        // If the current element in nums1 is greater than the current element in nums2
        if (nums1[i] > nums2[j]) {
            // Place the current element in nums1 at the end of the merged array
            nums1[k] = nums1[i];
            // Move the pointer in nums1 to the left
            i--;
        } else {
            // Place the current element in nums2 at the end of the merged array
            nums1[k] = nums2[j];
            // Move the pointer in nums2 to the left
            j--;
        }
        // Move the pointer in the merged array to the left
        k--;
    }

    // If there are remaining elements in nums2
    while (0 <= j) {
        // Place the remaining elements in nums2 at the beginning of the merged array
        nums1[k] = nums2[j];
        // Move the pointers in nums2 and the merged array to the left
        j--;
        k--;
    }
};
