/**
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
 * This module contains a function to find the kth smallest prime fraction from an array of numbers.
 */

/**
 * Function to find the kth smallest prime fraction from an array of numbers.
 *
 * @param arr - An array of numbers.
 * @param k - The kth smallest prime fraction to find.
 * @returns An array containing the numerator and denominator of the kth smallest prime fraction.
 *
 * The function works by using a binary search approach to find the kth smallest prime fraction.
 * It starts by initializing the left and right boundaries of the search, and the mid-point.
 * It then enters a loop where it calculates the total number of fractions that are less than or equal to mid,
 * and the maximum fraction that is less than or equal to mid.
 * If the total number of fractions is equal to k, it returns the maximum fraction.
 * If the total number of fractions is greater than k, it adjusts the right boundary to mid.
 * If the total number of fractions is less than k, it adjusts the left boundary to mid.
 * The loop continues until the left boundary is greater than the right boundary.
 * The function then returns the maximum fraction found.
 */
function kthSmallestPrimeFraction(arr: number[], k: number): number[] {
    // Initialize left and right boundaries for binary search, and the result array
    let left = 0, right = 1, mid: number, res = [], n = arr.length;

    // Start binary search
    while (left <= right) {
        // Calculate mid-point
        mid = left + (right - left) / 2;
        let maxFrac = 0, total = 0, j = 1, num = 0, den = 0;

        // Loop through the array
        for (let i = 0; i < n; i++) {
            // Find the position where arr[i] >= arr[j] * mid
            while (j < n && arr[i] >= arr[j] * mid) {
                ++j;
            }

            // Calculate the total number of fractions that are less than or equal to mid
            total += n - j

            // Find the maximum fraction that is less than or equal to mid
            if (j < n && maxFrac < arr[i] / arr[j]) {
                maxFrac = arr[i] / arr[j];
                num = i;
                den = j;
            }
        }

        // If the total number of fractions is equal to k, return the maximum fraction
        if (total === k) {
            res.push(arr[num]);
            res.push(arr[den]);
            return res;
        }

        // If the total number of fractions is greater than k, adjust the right boundary to mid
        if (total > k) {
            right = mid;
        } else {
            // If the total number of fractions is less than k, adjust the left boundary to mid
            left = mid;
        }
    }

    // Return the maximum fraction found
    return res;
}
