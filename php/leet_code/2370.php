<?php

/**
 * This module contains the Solution class which provides a method to find the longest ideal string.
 * The longest ideal string is defined as the longest string that can be formed from the input string
 * by only changing characters within a certain range.
 *
 * PHP version 8.3
 *
 * @category LeetCode
 * @package  LeetCode\Solution
 * @author   JerodG
 * @license  http://opensource.org/licenses/gpl-license.php GNU Public License
 * @link     http://github.com/jerodg/
 */

/**
 * Class Solution
 *
 * This class provides a method to find the longest ideal string.
 */
class Solution
{
    /**
     * Finds the longest ideal string.
     *
     * This method takes a string and an integer as input. It then calculates the longest ideal string
     * that can be formed from the input string by only changing characters within a range defined by the integer.
     * The method uses a dynamic programming approach to solve the problem.
     *
     * @param string $s The input string.
     * @param int $k The range within which characters can be changed.
     *
     * @return int The length of the longest ideal string.
     *
     * @throws InvalidArgumentException If the input string is not a string or the range is not an integer.
     */
    public function longestIdealString(string $s, int $k): int
    {
        // Initialize an array to keep track of the maximum length of the ideal string for each character.
        $db = array_fill(0, 26, 0);

        // Iterate over each character in the input string.
        for ($i = 0, $iMax = strlen($s); $i < $iMax; $i++) {
            // Calculate the index of the current character in the alphabet.
            $charIndex = ord($s[$i]) - ord('a');
            $maxLen = 1;

            // Iterate over each character within the range defined by $k.
            for ($j = max(0, $charIndex - $k); $j <= min(25, $charIndex + $k); $j++) {
                // Update the maximum length of the ideal string for the current character.
                $maxLen = max($maxLen, $db[$j] + 1);
            }

            // Update the maximum length of the ideal string for the current character in the database.
            $db[$charIndex] = max($db[$charIndex], $maxLen);
        }

        // Return the maximum length of the ideal string.
        return max($db);
    }
}
