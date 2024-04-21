<?php

declare(strict_types=1);

/**
 * This class provides a solution for finding the maximal rectangle in a binary matrix.
 */
class Solution
{
    /**
     * This method calculates the maximal rectangle in a binary matrix.
     *
     * @param array $matrix The binary matrix.
     * @return int The area of the maximal rectangle.
     */
    public function maximalRectangle(array $matrix): int
    {
        // Return 0 if the matrix is empty
        if (empty($matrix) || empty($matrix[0])) {
            return 0;
        }

        $rows = count($matrix);
        $cols = count($matrix[0]);

        // Initialize heights array with zeros
        $heights = array_fill(0, $cols + 1, 0);
        $maxArea = 0;

        for ($i = 0; $i < $rows; $i++) {
            $stack = [];
            for ($j = 0; $j <= $cols; $j++) {
                // Update the height of the current column.
                $heights[$j] = ($j < $cols && $matrix[$i][$j] === '1') ? ($heights[$j] + 1) : 0;

                // While the stack is not empty and the current height is less than the height at the top of the stack
                while (!empty($stack) && $heights[$j] < $heights[end($stack)]) {
                    // Pop the top of the stack and calculate the area
                    $height = $heights[array_pop($stack)];
                    $width = empty($stack) ? $j : $j - 1 - end($stack);
                    $maxArea = max($maxArea, $height * $width);
                }

                // Push the current index to the stack
                $stack[] = $j;
            }
        }

        // Return the maximum area
        return $maxArea;
    }
}
