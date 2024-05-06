/**
 * @file 26.c
 * @brief This module provides a function to remove duplicates from a sorted array.
 * @author JerodG <https://github.com/jerodg>
 * @date 04May24
 */

#pragma GCC optimize("O3,unroll-loops")

/**
 * @brief Removes duplicates from a sorted array.
 * @param nums The sorted array from which to remove duplicates.
 * @param numsSize The size of the nums array.
 * @return The new length of the array after duplicates have been removed.
 *
 * This function iterates over the nums array, comparing each element with the previous one. If the current element is different,
 * it is moved to the next position of the last non-duplicate element. The function returns the new length of the array after
 * duplicates have been removed.
 */
int removeDuplicates(int* nums, const int numsSize) {
    if (numsSize == 0) {
        return 0;
    }

    // Index of the last non-duplicate element
    int i = 0;

    // Iterate over the array, starting from the second element
    for (int j = 1; j < numsSize; j++) {
        // If the current element is different from the last non-duplicate element,
        // move it to the next position of the last non-duplicate element
        if (nums[j] != nums[i]) {
            nums[++i] = nums[j];
        }
    }

    // Return the new length of the array after duplicates have been removed
    return i + 1;
}
