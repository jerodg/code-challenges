/**
 * Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
 * <p>
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 * <p>
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 * <p>
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * This class provides a solution for finding the kth smallest prime fraction.
 */
class Solution {
    /**
     * This method finds the kth smallest prime fraction from an array of integers.
     *
     * @param arr The array of integers from which to find the kth smallest prime fraction.
     * @param k The rank of the smallest prime fraction to find.
     * @return An array of two integers representing the kth smallest prime fraction.
     */
    public static int[] kthSmallestPrimeFraction(final int[] arr, final int k) {
        final int n = arr.length;
        double left = 0, right = 1, mid;
        final int[] res = new int[2];

        // Binary search for the kth smallest prime fraction.
        while (left <= right) {
            mid = left + (right - left) / 2;
            int j = 1, total = 0, num = 0, den = 0;
            double maxFrac = 0;

            // Iterate over the array to find the total number of fractions less than or equal to mid.
            for (int i = 0; i < n; ++i) {
                while (j < n && arr[i] >= arr[j] * mid) {
                    ++j;
                }

                total += n - j;

                // Update the maximum fraction and its numerator and denominator.
                if (j < n && maxFrac < arr[i] * 1.0 / arr[j]) {
                    maxFrac = arr[i] * 1.0 / arr[j];
                    num = i;
                    den = j;
                }
            }

            // If the total number of fractions is equal to k, update the result and break the loop.
            if (total == k) {
                res[0] = arr[num];
                res[1] = arr[den];
                break;
            }

            // Update the search range based on the total number of fractions.
            if (total > k) {
                right = mid;
            } else {
                left = mid;
            }
        }

        return res;
    }
}
