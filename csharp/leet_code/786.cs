/*
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

/// <summary>
/// This class provides a solution for finding the Kth smallest prime fraction in an array.
/// </summary>
public class Solution {
    /// <summary>
    /// This method finds the Kth smallest prime fraction in an array.
    /// </summary>
    /// <param name="arr">An array of integers, sorted in ascending order.</param>
    /// <param name="k">The Kth smallest fraction to find.</param>
    /// <returns>An array of two integers representing the numerator and denominator of the Kth smallest fraction.</returns>
    public int[] KthSmallestPrimeFraction(int[] arr, int k) {
        int n = arr.Length;
        double left = 0, right = 1;
        int[] result = new int[2];

        // Binary search for the Kth smallest fraction
        while (right - left > 1e-9) {
            double mid = (left + right) / 2;
            int count = 0;
            double maxFraction = 0;
            int numerator = 0, denominator = 0;

            // Count fractions that are less than or equal to mid and find the maximum fraction
            for (int i = 0, j = 1; i < n - 1; i++) {
                while (j < n && arr[i] > mid * arr[j]) {
                    j++;
                }
                count += n - j;
                if (j < n && maxFraction < (double)arr[i] / arr[j]) {
                    maxFraction = (double)arr[i] / arr[j];
                    numerator = arr[i];
                    denominator = arr[j];
                }
            }

            // If count equals k, we found the Kth smallest fraction
            if (count == k) {
                result[0] = numerator;
                result[1] = denominator;
                break;
            }
            // If count is less than k, increase the lower bound
            else if (count < k) {
                left = mid;
            }
            // If count is greater than k, decrease the upper bound
            else {
                right = mid;
            }
        }

        return result;
    }
}
