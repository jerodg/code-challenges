/*
 *  Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 *  This program is free software: you can redistribute it and/or modify it under the terms of the
 *  Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 *  or (at your option) any later version.
 *
 *  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 *  even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 *  for more details.
 *
 *  The above copyright notice and this permission notice shall be included in all copies or
 *  substantial portions of the Software. You should have received a copy of the SSPL along with this
 *  program. If not, see SSPL.
 */

/**
 * Package leet_code
 *
 * This file contains the implementation of the `subsetXORSum` function.
 * The function calculates the sum of all possible XOR results of subsets of the given array of numbers.
 */

/**
 * Function to calculate the sum of all possible XOR results of subsets of a given array of numbers.
 *
 * @param {number[]} nums - The array of numbers.
 * @returns {number} - The sum of all possible XOR results of subsets of the array.
 *
 * @example
 *
 * subsetXORSum([1, 3])
 * // returns 6
 *
 * subsetXORSum([5, 1, 6])
 * // returns 28
 */
function subsetXORSum(nums: number[]): number {
    // Initialize the XOR result
    let a = 0;

    // Calculate the XOR result of all numbers in the array
    for (let n of nums) {
        a |= n;
    }

    // Multiply the XOR result by 2 to the power of (the length of the array minus 1) and return the result
    return a * Math.pow(2, nums.length - 1);
}
