/**
 * @fileoverview This module provides a function to find the kth smallest prime fraction from an array of sorted primes.
 * @author JerodG <https://github.com/jerodg/>
 * @module leet_code/786.mjs
 * @license Server Side Public License (SSPL)
 *
 * Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
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
 * program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * Function to find the kth smallest prime fraction from an array of sorted primes.
 * @param {Array} arr - The array of sorted primes.
 * @param {number} k - The kth smallest fraction to find.
 * @returns {Array} The kth smallest prime fraction as an array of two elements [numerator, denominator].
 */
const kthSmallestPrimeFraction = function (arr, k) {
    let left = 0, right = 1;
    let res = [];

    // Binary search for the kth smallest fraction
    while (left <= right) {
        let mid = left + (right - left) / 2;
        let j = 1, total = 0, num = 0, den = 0;
        let maxFrac = 0;

        // Count fractions less than mid and keep track of max fraction
        for (let i = 0; i < arr.length; ++i) {
            while (j < arr.length && arr[i] >= arr[j] * mid) {
                ++j;
            }
            total += arr.length - j;

            if (j < arr.length && maxFrac < arr[i] / arr[j]) {
                maxFrac = arr[i] / arr[j];
                num = i;
                den = j;
            }
        }

        // If total fractions is equal to k, we found the kth smallest fraction
        if (total === k) {
            res = [arr[num], arr[den]];
            break;
        }

        // If total fractions is more than k, search in the left half
        if (total > k) {
            right = mid;
        } else {
            // If total fractions is less than k, search in the right half
            left = mid;
        }
    }

    return res;
};
