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
#pragma GCC optimize("O3,unroll-loops")

/**
 * @file leet_code/1863.cpp
 * @brief This file contains the Solution class which is used to solve the problem of calculating the sum of
 * all possible XORs of subsets of a given array.
 * @package leet_code
 */

#include <vector>

/**
 * @class Solution
 * @brief This class is used to solve the problem of calculating the sum of all possible XORs of subsets of a given array.
 *
 * The class contains two methods: subsetXORSum and xor_sum. subsetXORSum is a public method that acts as an interface
 * for the user to input their array. xor_sum is a private method that performs the actual calculation.
 */
class Solution {
public:
    /**
     * @brief This method is used to start the calculation of the sum of all possible XORs of subsets of a given array.
     *
     * @param nums This is the input array of integers.
     * @return int The sum of all possible XORs of subsets of the input array.
     */
    static int subsetXORSum(std::vector<int>& nums) {
        return xor_sum(nums, 0, 0);
    }

private:
    /**
     * @brief This method is used to calculate the sum of all possible XORs of subsets of a given array.
     *
     * This method uses recursion to calculate the XOR sum. It considers two cases at each step: including the current
     * element in the XOR sum and excluding it. The base case is when the index equals the size of the array, in which
     * case it returns the current XOR sum.
     *
     * @param nums This is the input array of integers.
     * @param index This is the current index in the array.
     * @param current_xor This is the current XOR sum.
     * @return int The sum of all possible XORs of subsets of the input array.
     */
    static int xor_sum(std::vector<int>& nums, const int index, const int current_xor) {
        // Base case: if the index equals the size of the array, return the current XOR sum.
        if (index == nums.size()) return current_xor;

        // Recursive case 1: include the current element in the XOR sum.
        const int with_element = xor_sum(nums, index + 1, current_xor ^ nums[index]);

        // Recursive case 2: exclude the current element from the XOR sum.
        const int without_element = xor_sum(nums, index + 1, current_xor);

        // Return the sum of the XOR sums from both cases.
        return with_element + without_element;
    }
};
