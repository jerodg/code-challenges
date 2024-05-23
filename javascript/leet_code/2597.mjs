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
 * This file `2597.mjs` contains a function `beautifulSubsets` that calculates the number of beautiful subsets in an
 * array. A beautiful subset is defined as a subset where no two elements have a difference equal to `k`. It uses a
 * helper function `helper` to recursively calculate the number of beautiful subsets.
 */

/**
 * Function to calculate the number of beautiful subsets in an array.
 *
 * @param {number[]} nums - The array of numbers.
 * @param {number} k - The difference that should not exist between any two elements in a beautiful subset.
 * @returns {number} - The number of beautiful subsets in the array.
 */
const beautifulSubsets = function (nums, k) {
    /**
     * Helper function to recursively calculate the number of beautiful subsets.
     *
     * @param {number[]} arr - The array to calculate the number of beautiful subsets for.
     * @returns {number} - The number of beautiful subsets in the array.
     */
    const helper = arr => {
        // The length of the array.
        let len = arr.length;

        // If the array is empty, there are no beautiful subsets.
        if (len === 0) {
            return 0;
        }

        // The result variable to store the number of beautiful subsets.
        let res = 0;

        // Loop through the array.
        for (let i = 0; i < len; i++) {
            // The next array to pass to the recursive call.
            let next = [];

            // Loop through the rest of the array.
            for (let j = i + 1; j < len; j++) {
                // If the difference between the current element and the next element is not equal to `k`, add the next
                // element to the `next` array.
                if (Math.abs(arr[i] - arr[j]) !== k) {
                    next.push(arr[j]);
                }
            }

            // Add the number of beautiful subsets in the `next` array to the result.
            res += 1 + helper(next);
        }

        // Return the result.
        return res;
    };

    // Call the helper function with the `nums` array and return the result.
    return helper(nums);
};
