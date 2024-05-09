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
 * This class provides a solution for a problem related to maximizing happiness sum.
 * The problem is solved using binary search and quick sort algorithms.
 */
class Solution {
    /**
     * This method calculates the maximum happiness sum.
     *
     * @param happiness An array of integers representing happiness values.
     * @param k An integer representing the number of elements to consider.
     * @return The maximum possible sum of happiness.
     */
    public long maximumHappinessSum(final int[] happiness, final int k) {

        int left = 0, right = k;
        while (left < right) {
            final int mid = left + right >> 1;
            if (Solution.check(happiness, mid)) {
                left = mid + 1;
            } else
                right = mid;
        }

        int x = left;
        final int n = happiness.length;
        Solution.quickSort(happiness, 0, n - 1, n - x);
        long sum = -(long) x * (x - 1) >> 1;
        for (int i = n - 1; x-- > 0; --i)
            sum += happiness[i];

        return sum;
    }

    /**
     * This method checks if there are more than 'mid' elements in 'happiness' array that are greater than or equal to 'mid'.
     *
     * @param happiness An array of integers representing happiness values.
     * @param mid An integer representing the middle value.
     * @return True if there are more than 'mid' elements in 'happiness' that are greater than or equal to 'mid', false otherwise.
     */
    private static boolean check(final int[] happiness, final int mid) {
        int count = 0;
        for (final int x : happiness) {
            if (x < mid) continue;
            if (++count > mid)
                return true;
        }

        return false;
    }

    /**
     * This method sorts the 'nums' array using the quick sort algorithm.
     *
     * @param nums An array of integers to be sorted.
     * @param low An integer representing the lower bound of the part of the array to be sorted.
     * @param high An integer representing the upper bound of the part of the array to be sorted.
     * @param k An integer representing the number of elements to consider.
     */
    private static void quickSort(final int[] nums, final int low, final int high, final int k) {
        if (low == high)
            return;

        int left = low - 1;
        int right = high + 1;
        final int mid = low + high >> 1;
        final int x = nums[mid];
        while (left < right) {
            while (nums[++left] < x) continue;
            while (nums[--right] > x) continue;
            if (left < right) {
                final int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }
        }

        if (right < k)
            Solution.quickSort(nums, right + 1, high, k);
        else
            Solution.quickSort(nums, low, right, k);
    }
}
