<?php

declare(strict_types=1);

/**
 * Class Solution
 */
class Solution
{
    /**
     * This function removes k digits from the number to make it smallest.
     *
     * @param string $num The number from which digits are to be removed.
     * @param int $k The number of digits to remove.
     * @return string The smallest possible number after removing k digits.
     */
    public function removeKdigits(string $num, int $k): string
    {
        // Initialize an empty stack
        $stack = [];

        // Get the length of the number
        $len = strlen($num);

        // Iterate over each digit in the number
        for ($i = 0; $i < $len; $i++) {
            $n = $num[$i];

            // While there are still digits to remove and the top of the stack is greater than the current digit
            while ($k > 0 && count($stack) > 0 && $stack[count($stack) - 1] > $n) {
                // Remove the top digit from the stack
                array_pop($stack);
                // Decrease the count of digits to remove
                $k--;
            }

            // Add the current digit to the stack
            $stack[] = $n;
        }

        // If there are still digits to remove, remove them from the top of the stack
        while ($k > 0) {
            array_pop($stack);
            $k--;
        }

        // Convert the stack to a string
        $res = implode("", $stack);

        // Remove leading zeros
        $res = ltrim($res, "0");

        // If the result is an empty string, return "0", otherwise return the result
        return $res === "" ? "0" : $res;
    }
}
