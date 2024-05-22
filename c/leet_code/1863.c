/**
 * Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see SSPL.
 */

/**
 * @file leet_code/1863.c
 * @brief This file contains the implementation of the subsetXORSum function.
 *
 * The function calculates the XOR sum of all possible subsets of the given array.
 */
#pragma GCC optimize("O3,unroll-loops")
#include <stdio.h>

/**
 * @brief Recursive helper function to generate all subsets and calculate their XOR.
 *
 * This function is used by the subsetXORSum function to generate all possible subsets of the given array.
 * It calculates the XOR of each subset and adds it to the result.
 *
 * @param nums The input array.
 * @param nums_size The size of the input array.
 * @param index The current index in the array.
 * @param curr_xor The current XOR of the subset.
 * @param res Pointer to the result variable where the XOR sum of all subsets is stored.
 */
void gen_subset_xor(int *nums, const int nums_size,  const int index, const int curr_xor, int *res)
{
    // Base case: if the current index is equal to the size of the array, add the current XOR to the result and return.
    if (index == nums_size){
        *res += curr_xor;
        return;
    }

    // Recursive case: generate subsets including the current element and excluding the current element.
    gen_subset_xor(nums, nums_size, index+1, curr_xor ^ nums[index], res); // Include the current element.
    gen_subset_xor(nums, nums_size, index+1, curr_xor, res); // Exclude the current element.
}

/**
 * @brief Function to calculate the XOR sum of all possible subsets of the given array.
 *
 * This function uses the helper function gen_subset_xor to generate all possible subsets of the given array.
 * It calculates the XOR of each subset and returns the sum of all these XORs.
 *
 * @param nums The input array.
 * @param numsSize The size of the input array.
 * @return The XOR sum of all possible subsets of the array.
 */
int subsetXORSum(int* nums, const int numsSize) {
    int res = 0; // Variable to store the result.
    gen_subset_xor(nums, numsSize, 0, 0, &res); // Call the helper function to calculate the XOR sum.
    return res; // Return the result.
}
