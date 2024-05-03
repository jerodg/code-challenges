/**
 * @file leet_code/2441.cpp
 * @brief This module contains the Solution class which provides a method to
 * find the maximum absolute value in a sorted array.
 *
 * The Solution class has a single public method, findMaxK, which takes a vector
 * of integers and returns the maximum absolute value. If no such value exists,
 * it returns -1. The method assumes that the input vector is sorted in
 * ascending order.
 */
#pragma GCC optimize("O3,unroll-loops")
#include <algorithm>
#include <vector>

/**
 * @class Solution
 * @brief A class that provides a method to find the maximum absolute value in a
 * sorted array.
 */
class Solution {
public:
  /**
   * @brief Finds the maximum absolute value in a sorted array.
   *
   * This method takes a sorted vector of integers and finds the maximum
   * absolute value. It uses a two-pointer approach, starting from both ends of
   * the vector and moving towards the center. If the absolute value of the
   * number at the left pointer is equal to the number at the right pointer, it
   * returns that number. If the absolute value of the number at the left
   * pointer is greater than the number at the right pointer, it increments the
   * left pointer. If the absolute value of the number at the left pointer is
   * less than the number at the right pointer, it decrements the right pointer.
   * If no such number is found, it returns -1.
   *
   * @param nums A reference to a vector of integers. The vector is assumed to
   * be sorted in ascending order.
   * @return The maximum absolute value in the vector, or -1 if no such value
   * exists.
   */
  int findMaxK(std::vector<int> &nums) {
    std::ranges::sort(nums);

    int i = 0; // Left pointer, initialized to the start of the vector.
    int j =
        nums.size() - 1; // Right pointer, initialized to the end of the vector.

    // While the left pointer is less than the right pointer, and the number at
    // the left pointer is negative and the number at the right pointer is
    // positive...
    while (i < j && nums[i] < 0 && nums[j] > 0) {
      // If the absolute value of the number at the left pointer is equal to the
      // number at the right pointer...
      if (abs(nums[i]) == nums[j])
        return nums[j]; // Return that number.
      // If the absolute value of the number at the left pointer is greater than
      // the number at the right pointer...
      if (abs(nums[i]) > nums[j])
        i++; // Increment the left pointer.
      else
        j--; // Otherwise, decrement the right pointer.
    }

    return -1; // If no such number is found, return -1.
  }
};
