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
 * The Solution class contains methods for solving specific problems related to islands.
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
     * Calculates the perimeter of an island in a given grid.
     *
     * This method takes a 2D array representing a grid, where 1 represents land and 0 represents water.
     * It returns the total perimeter of the island.
     *
     * @param array $grid The grid representing the island.
     *
     * @return int The total perimeter of the island.
     *
     * @throws InvalidArgumentException If $grid is not a 2D array.
     *
     * @example
     * $solution = new Solution();
     * $perimeter = $solution->islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]);
     * echo $perimeter; // Outputs: 16
     */
    function islandPerimeter(array $grid): int
    {
        // Count the number of columns in the grid
        $cols = count($grid[0]);
        // Initialize the perimeter and neighbors count
        $perimeter = 0;
        $neighbors = 0;

        // Iterate over each cell in the grid
        foreach ($grid as $row => $rowValue) {
            for ($col = 0; $col < $cols; $col++) {
                // If the cell is land
                if ($rowValue[$col] == 1) {
                    // Add 4 to the perimeter (for each side of the cell)
                    $perimeter += 4;

                    // If the cell to the left is also land, increment the neighbors count
                    if ($col > 0 && $rowValue[$col - 1] == 1) {
                        $neighbors++;
                    }

                    // If the cell above is also land, increment the neighbors count
                    if ($row > 0 && $grid[$row - 1][$col] == 1) {
                        $neighbors++;
                    }
                }
            }
        }
        // Subtract twice the neighbors count from the perimeter (since each neighbor reduces the perimeter by 2)
        return $perimeter - 2 * $neighbors;
    }
}
