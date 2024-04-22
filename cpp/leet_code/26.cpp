/**
 * @file 26.cpp
 * @brief This file contains the solution for removing duplicates from a sorted array.
 */
// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <vector>

/**
 * @class Solution
 * @brief This class contains the method to remove duplicates from a sorted array.
 */
class Solution {
public:
    /**
     * @brief This method removes duplicates from a sorted array in-place such that each element appears only once and returns the new length.
     * @param nums A reference to the vector of integers.
     * @return The new length of the array after removing duplicates.
     * @note Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
     * @note The order of elements can be changed. It doesn't matter what you leave beyond the new length.
     */
    static int removeDuplicates(std::vector<int> &nums) {
        if (nums.size() != 0) {
            return 0;
        }
        int i = 0;
        for (int j = 1; j < nums.size(); j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
};
