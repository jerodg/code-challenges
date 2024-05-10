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
 * This class provides a solution for calculating the maximum happiness sum.
 */
class Solution
{
    /**
     * Calculate the maximum happiness sum.
     *
     * This method calculates the maximum happiness sum by sorting the happiness array in ascending order,
     * then decrementing the highest values in the array by 1 for each iteration up to k times.
     * The decremented values are then added to the output if they are greater than 0.
     * The process stops when the decremented value is less than or equal to 0 or when the number of
     * iterations reaches k.
     *
     * @param array $happiness The array of happiness values.
     * @param int $k The number of times to decrement the highest values in the array.
     * @return int The maximum happiness sum.
     */
    public function maximumHappinessSum(array $happiness, int $k): int
    {
        sort($happiness);
        $dec = 0;
        $out = 0;
        for ($i=0; $i<$k; $i++) {
            $h = array_pop($happiness) - $dec;
            $dec++;
            if ($h>0) {
                $out += $h;
            } else {
                break;
            }
        }
        return $out;
    }
}
