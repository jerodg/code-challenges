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
 * Package leet_code
 *
 * This file `1863.mjs` contains a function `subsetXORSum` that calculates the sum of all possible XOR results of
 * subsets of the input array. It uses a helper function `findSum` to recursively calculate the XOR sum.
 */

/**
 * Function to calculate the sum of all possible XOR results of subsets of the input array.
 *
 * @param {number[]} nums - The array of numbers.
 * @returns {number} - The sum of all possible XOR results of subsets of the input array.
 */
const subsetXORSum = function (nums) {
    return findSum(nums, 0, 0);
};

/**
 * Helper function to recursively calculate the XOR sum.
 *
 * @param {number[]} nums - The array of numbers.
 * @param {number} curInd - The current index in the array.
 * @param {number} curNum - The current number.
 * @returns {number} - The XOR sum.
 */
function findSum(nums, curInd, curNum) {
    // If the current index is equal to the length of the array, return the current number.
    if (curInd === nums.length) {
        return curNum;
    }

    // Calculate the XOR sum when the current number is included in the XOR operation.
    let includeInXor = findSum(nums, curInd + 1, curNum ^ nums[curInd]);
    // Calculate the XOR sum when the current number is not included in the XOR operation.
    let notIncludeInXor = findSum(nums, curInd + 1, curNum);

    // Return the sum of the XOR sums when the current number is included and not included in the XOR operation.
    return includeInXor + notIncludeInXor;
}
