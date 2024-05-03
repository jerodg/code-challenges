/**
 * @file leet_code/2441.c
 * @brief This module provides a function to find the maximum positive integer
 * that also has a negative counterpart in an array.
 *
 * The function `findMaxK` takes an array of integers and its size as input, and
 * returns the maximum positive integer that also has a negative counterpart in
 * the array. If no such integer exists, it returns -1.
 */

#include <stdlib.h>

/**
 * @brief Finds the maximum positive integer that also has a negative
 * counterpart in an array.
 *
 * This function iterates over the array twice. In the first iteration, it marks
 * the absolute values of negative numbers in a separate array. In the second
 * iteration, it checks for each positive number if it was marked in the first
 * iteration and if it is greater than the current maximum. If both conditions
 * are met, it updates the maximum.
 *
 * @param nums Pointer to the array of integers.
 * @param numsSize The size of the array.
 * @return The maximum positive integer that also has a negative counterpart in
 * the array, or -1 if no such integer exists.
 */
int findMaxK(const int *nums, const int numsSize) {
  int maxk = -1; // The current maximum positive integer that also has a
                 // negative counterpart in the array.
  int arr[1001] = {
      0}; // An array to mark the absolute values of negative numbers.

  // First iteration: mark the absolute values of negative numbers.
  for (int i = 0; i < numsSize; i++) {
    if (nums[i] < 0)
      arr[abs(nums[i])] = 1;
  }

  // Second iteration: find the maximum positive integer that also has a
  // negative counterpart.
  for (int i = 0; i < numsSize; i++) {
    if (arr[abs(nums[i])] == 1 && maxk < nums[i] && nums[i] > 0)
      maxk = nums[i];
  }

  return maxk; // Return the maximum positive integer that also has a negative
               // counterpart, or -1 if no such integer exists.
}
