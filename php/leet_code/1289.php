<?php

/**
 * This module contains the Solution class which provides a method to find the minimum falling path sum in a grid.
 * The method uses dynamic programming to calculate the minimum sum of each path from the top to the bottom of the grid.
 * The minimum falling path sum is then returned.
 */

class Solution
{
    /**
     * This method finds the minimum falling path sum in a grid.
     *
     * @param array $grid A 2D array of integers representing the grid.
     * @return int The minimum falling path sum in the grid.
     */
    public function minFallingPathSum(array $grid): int
    {
        // Get the size of the grid
        $n = count($grid);

        // If the grid only contains one element, return that element
        if ($n == 1) {
            return $grid[0][0];
        }

        // Initialize a 2D array to store the minimum sum of each path
        $rs = [[], []];

        // Initialize the 2D array with 0
        for ($i = 0; $i < $n; ++$i) {
            $rs[1][] = 0;
            $rs[0][] = 0;
        }

        // Iterate over each row in the grid
        foreach ($grid as $i => $iValue) {
            // Get the current row in the 2D array
            $r0 = &$rs[$i & 1];

            // Initialize the two smallest values in the current row to the maximum integer value
            $min2 = PHP_INT_MAX;
            $min1 = PHP_INT_MAX;

            // Find the two smallest values in the current row
            for ($j = 0; $j < $n; ++$j) {
                $r0j = $r0[$j];
                if ($r0j < $min1) {
                    $min2 = $min1;
                    $min1 = $r0j;
                } else if ($r0j < $min2) {
                    $min2 = $r0j;
                }
            }

            // Get the next row in the 2D array
            $r1 = &$rs[1 - ($i & 1)];

            // Get the current row in the grid
            $row = &$iValue;

            // Calculate the minimum sum of each path in the next row
            for ($j = 0; $j < $n; ++$j) {
                $r1[$j] = ($r0[$j] == $min1 ? $min2 : $min1) + $row[$j];
            }
        }

        // Initialize the minimum falling path sum to the maximum integer value
        $r = PHP_INT_MAX;

        // Find the minimum falling path sum
        foreach ($rs[$n & 1] as $ri) {
            if ($ri < $r) {
                $r = $ri;
            }
        }

        // Return the minimum falling path sum
        return $r;
    }
}
