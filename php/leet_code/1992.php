<?php

/**
 * This file contains the Solution class.
 *
 * PHP version 8.3
 *
 * @category LeetCode
 * @package  LeetCode\Solution
 * @author   Jerodg
 * @license  http://opensource.org/licenses/gpl-license.php GNU Public License
 * @link     http://github.com/jerodg/leet_code
 */

declare(strict_types=1);

/**
 * The Solution class contains methods for solving specific problems related to farmland.
 *
 * @category LeetCode
 * @package  LeetCode\Solution
 * @author   Jerodg
 * @license  http://opensource.org/licenses/gpl-license.php GNU Public License
 * @link     http://github.com/jerodg/leet_code
 */
class Solution
{
    /**
     * Finds the farmland in a given land matrix.
     *
     * This method takes a 2D array representing a land matrix, where 1 represents farmland and 0 represents non-farmland.
     * It returns an array of farmlands, where each farmland is represented as an array [i, j, x, y] where (i, j) is the top-left corner of the farmland and (x, y) is the bottom-right corner of the farmland.
     *
     * @param array $land The land matrix.
     *
     * @return array The array of farmlands.
     *
     * @throws InvalidArgumentException If $land is not a 2D array.
     *
     * @example
     * $solution = new Solution();
     * $farmlands = $solution->findFarmland([[1,0,0],[0,1,1],[0,1,1]]);
     * print_r($farmlands); // Outputs: [[0,0,0,0],[1,1,2,2]]
     */
    public function findFarmland(array $land): array
    {
        // Initialize the output array
        $output = [];

        // Calculate the number of columns in the land matrix
        $numColumns = count($land[0]);

        // Iterate over each row in the land matrix
        foreach ($land as $i => $iValue) {

            // Iterate over each column in the current row
            for ($j = 0; $j < $numColumns; $j++) {

                // Get the current cell value
                $n = $iValue[$j];

                // Check if the current cell is the top-left corner of a farmland
                if ($n && ($i == 0 || $land[$i - 1][$j] == 0) && ($j == 0 || $iValue[$j - 1] == 0)) {

                    // Initialize the bottom-right corner of the farmland
                    $x = $i;
                    $y = $j;

                    // Find the bottom boundary of the farmland
                    while ($x < count($land) - 1 && $land[$x + 1][$y] == 1) {
                        $x++;
                    }

                    // Find the right boundary of the farmland
                    while ($y < $numColumns - 1 && $land[$x][$y + 1] == 1) {
                        $y++;
                    }

                    // Add the farmland to the output array
                    $output[] = [$i, $j, $x, $y];
                }
            }
        }

        // Return the output array
        return $output;
    }
}
