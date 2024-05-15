/**
 * @file leet_code/786.c
 * @brief This file contains the implementation of a function to find the Kth smallest prime fraction among all prime fractions that can be formed by taking the fractions of numbers in a sorted array.
 *
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
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
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */

#pragma GCC optimize("O3,unroll-loops")

#include <stdlib.h>

/**
 * @brief Finds the Kth smallest prime fraction among all prime fractions that can be formed by taking the fractions of numbers in a sorted array.
 *
 * @param arr The sorted array.
 * @param arrSize The size of the array.
 * @param k The Kth smallest prime fraction to find.
 * @param returnSize The size of the returned array.
 * @return int* The Kth smallest prime fraction.
 */
int* kthSmallestPrimeFraction(const int* arr, int arrSize, int k, int* returnSize) {
    // Allocate memory for the result
    int* res = malloc(sizeof(int) * 2);
    *returnSize = 2;

    // Initialize the left and right boundaries for the binary search
    double l = 0.0;
    double r = 1.0;

    // Perform binary search
    while (l < r) {
        double m = (l + r) / 2;
        double maxFraction = 0.0;
        int count = 0;
        int i = 0, j = 0;
        int q = 1;

        // Loop through the array
        for (int p = 0; p < arrSize - 1; ++p) {
            // Find the first fraction that is less than or equal to m
            while (q < arrSize && arr[p] >= m * arr[q]) {
                ++q;
            }

            // Count the number of fractions that are less than or equal to m
            count += arrSize - q;

            // If all fractions are less than or equal to m, break the loop
            if (q == arrSize) {
                break;
            }

            // Update the maximum fraction and its indices
            double fraction = arr[p] * 1.0 / arr[q];
            if (fraction > maxFraction) {
                i = p;
                j = q;
                maxFraction = fraction;
            }
        }

        // If the count is equal to k, return the maximum fraction
        if (count == k) {
            res[0] = arr[i];
            res[1] = arr[j];
            break;
        } else if (count > k) {
            // If the count is greater than k, update the right boundary
            r = m;
        } else {
            // If the count is less than k, update the left boundary
            l = m;
        }
    }

    return res;
}
