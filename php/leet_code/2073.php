<?php

/**
 * This module contains the Solution class which provides a method to calculate the time required to buy tickets.
 *
 * The Solution class has a single public method timeRequiredToBuy which takes an array of tickets and an integer k as input.
 * It calculates the time required to buy tickets based on the given conditions.
 *
 * PHP version 7
 *
 * @category   LeetCode
 * @package    Solution
 * @author     Jerodg
 * @license    https://opensource.org/licenses/MIT MIT License
 * @link       http://github.com/jerodg/leet_code/2073.php
 */

declare(strict_types=1);

class Solution
{
    /**
     * Calculate the time required to buy tickets.
     *
     * This function calculates the time required to buy tickets based on the given conditions.
     * It iterates over the tickets array and for each ticket, it checks if the value is greater than or equal to the target ticket.
     * If it is, it sets the time to the target ticket value. If the index is greater than k, it subtracts 1 from the time.
     * If the ticket value is less than the target ticket, it sets the time to the ticket value.
     * It then adds the time to the total time in line.
     * Finally, it returns the total time in line.
     *
     * @param array $tickets The array of tickets.
     * @param int $k The target ticket index.
     * @return int The total time required to buy tickets.
     * @throws InvalidArgumentException If the tickets array is empty or if k is not a valid index in the tickets array.
     *
     * @example
     * ```php
     * $solution = new Solution();
     * $time = $solution->timeRequiredToBuy([1, 2, 3, 4, 5], 2);
     * echo $time;  // Outputs: 10
     * ```
     */
    public function timeRequiredToBuy(array $tickets, int $k): int
    {
        if (empty($tickets)) {
            throw new InvalidArgumentException('Tickets array cannot be empty.');
        }

        if (!isset($tickets[$k])) {
            throw new InvalidArgumentException('Invalid index k.');
        }

        $time_in_line = 0;
        $tickets_target = $tickets[$k];

        foreach ($tickets as $i => $iValue) {
            // If the ticket value is greater than or equal to the target ticket
            if ($iValue >= $tickets_target) {
                $time = $tickets_target;
                // If the index is greater than k
                if ($i > $k) {
                    $time = $tickets_target - 1;
                }
            } else {
                // If the ticket value is less than the target ticket
                $time = $iValue;
            }
            // Add the time to the total time in line
            $time_in_line += $time;
        }

        // Return the total time in line
        return $time_in_line;
    }
}
