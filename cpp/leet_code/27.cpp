/**
 * @file 27.cpp
 * @brief This file contains the solution for removing a specific element from an array.
 */
// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <vector>

/**
 * @class Solution
 * @brief This class contains the method to remove a specific element from an array.
 */
class Solution {
public:
    /**
     * @brief This method removes all instances of a specific value in-place from an array and returns the new length.
     * @param nums A reference to the vector of integers.
     * @param val The value to be removed from the array.
     * @return The new length of the array after removing the specific value.
     * @note Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
     * @note The order of elements can be changed. It doesn't matter what you leave beyond the new length.
     */
    static int removeElement(std::vector<int>& nums, int val) {
        int i = 0;
        // Iterate over the array
        for (int j = 0; j < nums.size(); j++) {
            // If the current element is not the value to be removed, move it to the beginning of the array
            if (nums[j] != val) {
                nums[i++] = nums[j];
            }
        }
        // Return the new length of the array
        return i;
    }
};
