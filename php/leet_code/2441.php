<?php

/**
 * This module contains the Solution class which provides a method to find the maximum absolute value in an array
 * that appears exactly once. The method uses a hashmap to track the occurrence of each absolute value in the array.
 * If an absolute value appears more than once, it is set to 0 in the hashmap. The maximum absolute value that appears
 * exactly once is then returned.
 */

class Solution
{
    /**
     * This method finds the maximum absolute value in an array that appears exactly once.
     *
     * @param Integer[] $nums An array of integers. The array may contain both positive and negative numbers.
     * @return Integer The maximum absolute value in the array that appears exactly once. If no such value exists, -1 is returned.
     */
    public function findMaxK(array $nums): int
    {
        // Initialize a hashmap to track the occurrence of each absolute value in the array
        $map = [];
        // Initialize the maximum absolute value that appears exactly once to -1
        $max = -1;

        // Iterate over each number in the array
        foreach ($nums as $num) {
            // Get the absolute value of the number
            $index = abs($num);

            // If the absolute value is not in the hashmap, add it to the hashmap
            if (!array_key_exists($index, $map)) {
                $map[$index] = $num;
                continue;
            }

            // If the absolute value is already in the hashmap and its value is 0, skip it
            if ($map[$index] === 0) {
                continue;
            }

            // If the absolute value is already in the hashmap and its value is the same as the current number, skip it
            if ($map[$index] === $num) {
                continue;
            }

            // If the absolute value is already in the hashmap and its value is different from the current number,
            // set its value to 0 in the hashmap and update the maximum absolute value if necessary
            $map[$index] = 0;
            if ($index > $max) {
                $max = $index;
            }
        }

        // Return the maximum absolute value that appears exactly once
        return $max;
    }
}
