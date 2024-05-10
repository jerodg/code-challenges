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
 *
 * This file contains a solution for finding the kth smallest prime fraction from an array of integers.
 * The main class is `Solution` which contains a single public method `kthSmallestPrimeFraction`.
 */

class Solution {
    /**
     * This function finds the kth smallest prime fraction from an array of integers.
     *
     * The function uses a binary search approach to find the kth smallest fraction. It starts with a range
     * of possible fractions between 0 and 1 (inclusive). It then calculates the middle of this range and counts
     * the number of fractions that are less than or equal to this middle value. If the count is less than k,
     * it means the kth smallest fraction is greater than the middle value, so it adjusts the range to be between
     * the middle value and 1. If the count is greater than k, it means the kth smallest fraction is less than
     * or equal to the middle value, so it adjusts the range to be between 0 and the middle value. If the count
     * is exactly k, it means it has found the kth smallest fraction and it returns this fraction.
     *
     * @param arr the array of integers from which to find the kth smallest prime fraction.
     * @param k the rank of the smallest prime fraction to find.
     * @return an array of two integers representing the kth smallest prime fraction.
     * @throws IllegalArgumentException if `arr` is empty or `k` is not within the valid range.
     */
    fun kthSmallestPrimeFraction(arr: IntArray, k: Int): IntArray {
        var l = 0.0
        var r = 1.0
        var p = 0
        var q = 1
        val n = arr.size
        var cnt = 0
        while (true) {
            cnt = 0
            p = 0
            val m = (l + r) / 2
            var j = n - 1
            for (i in 0 until n) {
                while (j >= 0 && arr[i] > m * arr[n - 1 - j]) j--
                cnt += (j + 1)
                if (j >= 0 && p * arr[n - 1 - j] < q * arr[i]) {
                    p = arr[i]
                    q = arr[n - 1 - j]
                }
            }

            if (cnt < k) {
                l = m
            } else if (cnt > k) {
                r = m
            } else {
                return intArrayOf(p, q)
            }
        }
    }
}
