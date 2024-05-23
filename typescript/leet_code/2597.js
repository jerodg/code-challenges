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
 *
 */
/**
 * Package leet_code
 *
 * This file contains the implementation of the `beautifulSubsets` function.
 * The function calculates the total number of beautiful subsets in a given array of numbers.
 * A subset is considered beautiful if the difference between the maximum and minimum numbers in the
 * subset is equal to `k`.
 */
/**
 * Function to calculate the total number of beautiful subsets in a given array of numbers.
 *
 * @param {number[]} nums - The array of numbers.
 * @param {number} k - The difference between the maximum and minimum numbers in a subset to be considered beautiful.
 * @returns {number} - The total number of beautiful subsets in the array.
 *
 * @example
 *
 * beautifulSubsets([1, 2, 3, 4], 1)
 * // returns 15
 *
 * beautifulSubsets([1, 2, 3, 4], 2)
 * // returns 9
 */
function beautifulSubsets(nums, k) {
    // Initialize total count of beautiful subsets
    var totCount = 1;
    // Initialize a frequency map to store the frequency of each remainder when a number is divided by `k`
    var freqMap = new Map();
    // Populate the frequency map
    for (var _i = 0, nums_1 = nums; _i < nums_1.length; _i++) {
        var num = nums_1[_i];
        var remainder = num % k;
        if (!freqMap.has(remainder)) {
            freqMap.set(remainder, new Map());
        }
        var remainderMap = freqMap.get(remainder);
        remainderMap.set(num, (remainderMap.get(num) || 0) + 1);
    }
    // Calculate the total count of beautiful subsets
    for (var _a = 0, _b = freqMap.values(); _a < _b.length; _a++) {
        var fr = _b[_a];
        var subsets = Array.from(fr.entries()).sort(function (a, b) { return a[0] - b[0]; });
        var n = subsets.length;
        var currCount = 1;
        var next1 = 1;
        var next2 = 0;
        for (var i = n - 1; i >= 0; i--) {
            var skip = next1;
            var take = (1 << subsets[i][1]) - 1;
            if (i + 1 < n && subsets[i + 1][0] - subsets[i][0] === k) {
                take *= next2;
            }
            else {
                take *= next1;
            }
            currCount = skip + take;
            next2 = next1;
            next1 = currCount;
        }
        totCount *= currCount;
    }
    // Subtract 1 from the total count to exclude the empty subset and return the result
    return totCount - 1;
}
