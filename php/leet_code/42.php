<?php

declare(strict_types=1);

/**
 * This class provides a solution for the trapping rain water problem.
 */
class Solution
{
    /**
     * This method calculates the total amount of water that can be trapped.
     *
     * @param int[] $height An array of non-negative integers representing the elevation at each index.
     * @return int The total amount of water that can be trapped.
     */
    public function trap(array $height): int
    {
        $left = 0;
        $right = count($height) - 1;
        $res = 0;
        $left_max = $height[$left];
        $right_max = $height[$right];

        // Iterate until the left pointer is less than the right pointer
        while ($left < $right) {
            // If the maximum height on the left is less than the maximum height on the right
            if ($left_max < $right_max) {
                $left += 1;
                // Update the maximum height on the left
                $left_max = max($left_max, $height[$left]);
                // Add the difference between the maximum height on the left and the current height to the result
                $res += $left_max - $height[$left];
            } else {
                $right -= 1;
                // Update the maximum height on the right
                $right_max = max($right_max, $height[$right]);
                // Add the difference between the maximum height on the right and the current height to the result
                $res += $right_max - $height[$right];
            }
        }
        // Return the total amount of water that can be trapped
        return $res;
    }
}