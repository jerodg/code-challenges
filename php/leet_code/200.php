<?php

/**
 * This file contains the Solution class which includes methods for solving
 * specific problems related to graph traversal and island counting.
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
 * The Solution class contains methods for solving specific problems related to
 * graph traversal and island counting.
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
     * Counts the number of islands in a 2D grid map of '1's (land) and '0's (water).
     *
     * @param array $grid The 2D grid map of '1's (land) and '0's (water).
     *
     * @return int The number of islands.
     *
     * @throws InvalidArgumentException If $grid is not an array.
     *
     * @example
     * $solution = new Solution();
     * $numIslands = $solution->numIslands([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]);
     * echo $numIslands; // Outputs: 1
     */
    public function numIslands(array $grid): int
    {
        $count = 0;
        for ($i = 0, $iMax = count($grid); $i < $iMax; $i++) {
            for ($j = 0, $jMax = count($grid[0]); $j < $jMax; $j++) {
                if ($grid[$i][$j] === '1') {
                    $count++;
                    $this->makeWater($grid, $i, $j);
                }
            }
        }
        return $count;
    }

    /**
     * Converts a land cell ('1') into a water cell ('0') and does the same for its adjacent land cells.
     *
     * @param array $grid The 2D grid map of '1's (land) and '0's (water).
     * @param int $i The row index of the grid.
     * @param int $j The column index of the grid.
     *
     * @return void
     *
     * @throws InvalidArgumentException If $grid is not an array or $i and $j are not integers.
     *
     * @example
     * $solution = new Solution();
     * $solution->makeWater([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']], 0, 0);
     */
    public function makeWater(array &$grid, int $i, int $j): void
    {
        $grid[$i][$j] = '0';
        if ($grid[$i + 1][$j] === '1') {
            $this->makeWater($grid, $i + 1, $j);
        }
        if ($grid[$i - 1][$j] === '1') {
            $this->makeWater($grid, $i - 1, $j);
        }
        if ($grid[$i][$j + 1] === '1') {
            $this->makeWater($grid, $i, $j + 1);
        }
        if ($grid[$i][$j - 1] === '1') {
            $this->makeWater($grid, $i, $j - 1);
        }
    }
}
