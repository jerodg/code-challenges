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

using System;

/// <summary>
/// The Solution class contains methods to solve the problem of finding the maximum happiness sum.
/// </summary>
public class Solution {
    /// <summary>
    /// This method calculates the maximum happiness sum that can be obtained by selecting k elements from the happiness array.
    /// </summary>
    /// <param name="happiness">An array of integers representing the happiness values.</param>
    /// <param name="k">The number of elements to select from the happiness array.</param>
    /// <returns>The maximum happiness sum that can be obtained by selecting k elements from the happiness array.</returns>
    public long MaximumHappinessSum(int[] happiness, int k) {
        // Sort the happiness array in ascending order
        Array.Sort(happiness);
        long total = 0;
        int sub = 0;

        // Iterate over the happiness array from the end to the start
        for (int i = happiness.Length - 1; i >= 0 && k > 0; i--) {
            // Decrement k
            k--;
            // Add the maximum between the current happiness value minus the difference between the length of the happiness array and the current index, and 0, to the total
            total += Math.Max(happiness[i] - (happiness.Length - 1 - i), 0);
            // Increment sub
            sub++;
        }
        // Return the total happiness sum
        return total;
    }
}
