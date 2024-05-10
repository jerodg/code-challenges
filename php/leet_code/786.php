<?php
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

declare(strict_types=1);

/**
 * Class Solution
 *
 * This class provides a solution for finding the Kth smallest prime fraction in an array.
 */
class Solution
{
    /**
     * Find the Kth smallest prime fraction in an array.
     *
     * This method uses a binary search approach to find the Kth smallest prime fraction in an array.
     * It iterates over the array, comparing each element with the mid-point of the current search range.
     * If the current element divided by the next element is greater than the mid-point, it increments the
     * count and updates the max fraction.
     * If the count is equal to K, it returns the max fraction.
     * If the count is less than K, it updates the left boundary of the search range to the mid-point.
     * If the count is greater than K, it updates the right boundary of the search range to the mid-point.
     *
     * @param array $arr The array of integers.
     * @param int $k The Kth smallest prime fraction to find.
     * @return array The Kth smallest prime fraction, or an empty array if not found.
     */
    public function kthSmallestPrimeFraction($arr, $k): array
    {
        $n = count($arr);
        $left = 0.0;
        $right = 1.0;
        $result = [];

        while ($left < $right) {
            $mid = ($left + $right) / 2;
            $count = 0;
            $maxFraction = [0, 1];

            for ($i = 0, $j = 1; $i < $n - 1; $i++) {
                while ($j < $n && $arr[$i] / $arr[$j] > $mid) {
                    $j++;
                }
                $count += $n - $j;
                if ($j < $n && $arr[$i] / $arr[$j] > $maxFraction[0] / $maxFraction[1]) {
                    $maxFraction = [$arr[$i], $arr[$j]];
                }
            }

            if ($count == $k) {
                return $maxFraction;
            }

            if ($count < $k) {
                $left = $mid;
            } else {
                $right = $mid;
            }
        }
        return $result;
    }
}
