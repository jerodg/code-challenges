<?php
declare(strict_types=1);

/**
 * Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the Server Side Public License (SSPL) as
 * published by MongoDB, Inc., either version 1 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * SSPL for more details.
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * You should have received a copy of the SSPL along with this program.
 * If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * Class Solution
 *
 * This class provides a solution for calculating the minimum number of boats required
 * to rescue people based on their weights and the weight limit of each boat.
 */
class Solution
{
    /**
     * Calculates the minimum number of boats required to rescue people.
     *
     * The function sorts the array of people's weights in ascending order and uses a two-pointer technique
     * to calculate the minimum number of boats. It increments the total number of boats for each pair of people
     * that can fit in a single boat, or for each individual that requires a separate boat.
     *
     * @param array $people An array of integers representing the weights of each person.
     * @param int $limit The maximum weight that a single boat can carry.
     * @return int The minimum number of boats required.
     */
    public function numRescueBoats(array $people, int $limit): int
    {
        sort($people);
        $totalBoats = 0;
        $left = 0;
        $right = count($people) - 1;

        while ($left <= $right) {
            if ($people[$left] + $people[$right] <= $limit) {
                $left++;
            }
            $right--;
            $totalBoats++;
        }

        return $totalBoats;
    }
}
