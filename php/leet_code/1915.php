<?php

/**
 * This module contains the Solution class which provides a method to find the number of wonderful substrings in a word.
 * A wonderful string is a string where at most one letter appears an odd number of times.
 * The method uses bitwise operations and prefix counts to calculate the number of wonderful substrings.
 */

class Solution
{
    /**
     * This method finds the number of wonderful substrings in a word.
     *
     * @param string $word A string of lowercase English letters.
     * @return int The number of wonderful substrings in the word.
     */
    public function wonderfulSubstrings(string $word): int
    {
        // Initialize an array to store the prefix counts
        $prefixCount = [1];
        for ($i = 1; $i < 1024; ++$i) {
            $prefixCount[] = 0;
        }

        // Initialize the prefix to 0
        $prefix = 0;

        // Iterate over each character in the word
        foreach (str_split($word) as $c) {
            // Update the prefix using bitwise XOR operation
            $prefix ^= 1 << (ord($c) - 0x61);
            // Increment the prefix count
            ++$prefixCount[$prefix];
        }

        // Initialize the result to 0
        $r = 0;

        // Calculate the number of wonderful substrings
        for ($prefix = 0; $prefix < 1024; ++$prefix) {
            $a = $prefixCount[$prefix];
            $b = $a - 1;
            for ($i = 0; $i < 10; ++$i) {
                $b += $prefixCount[$prefix ^ (1 << $i)];
            }
            $r += $a * $b;
        }

        // Return the number of wonderful substrings
        return $r >> 1;
    }
}
