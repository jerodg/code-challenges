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
 * This file contains a solution for calculating the maximum happiness sum from an array of integers.
 * The main class is `Solution` which contains a single public method `maximumHappinessSum`.
 */

class Solution {
    /**
     * This function calculates the maximum happiness sum from an array of integers.
     *
     * The function first sorts the array in ascending order. It then initializes a sum to 0 and a size to k.
     * It iterates over the array in reverse order. For each element, if the size is greater than 0, it adds
     * the maximum of 0 and the difference between the current element and the minimum of k and the difference
     * between the size of the array and the current index to the sum. It then decrements the size. If the size
     * is not greater than 0, it breaks the loop. Finally, it returns the sum.
     *
     * @param happiness the array of integers representing happiness values.
     * @param k the number of elements to consider for the sum.
     * @return the maximum happiness sum.
     * @throws IllegalArgumentException if `happiness` is empty or `k` is not within the valid range.
     */
    fun maximumHappinessSum(happiness: IntArray, k: Int): Long {
        happiness.sort()
        var sum = 0L
        var size = k
        for (i in happiness.size - 1 downTo 0) {
            if (size > 0) {
                sum += Math.max(0, happiness[i] - Math.min(k, happiness.size - 1 - i))
                size--
            } else break
        }
        return sum
    }
}
