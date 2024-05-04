import java.util.Arrays;

/** This class provides a solution for finding the maximal rectangle in a binary matrix. */
class Solution {
    /**
     * Finds the maximal rectangle in a binary matrix.
     *
     * @param matrix The binary matrix.
     *
     * @return The area of the maximal rectangle.
     */
    public static int maximalRectangle(final char[][] matrix) {
        // If the matrix is null or empty, return 0
        if (null == matrix || 0 == matrix.length || 0 == matrix[0].length) {
            return 0;
        }

        final int m = matrix.length;
        final int n = matrix[0].length;

        // Initialize arrays to store heights and boundaries of rectangles
        final int[] heights = new int[n];
        final int[] leftBoundaries = new int[n];
        final int[] rightBoundaries = new int[n];
        Arrays.fill(rightBoundaries, n);

        int maxRectangle = 0;

        // Iterate over each row in the matrix
        for (final char[] chars : matrix) {
            final int left = 0;

            // Update heights and left boundaries for each row
            Solution.updateHeightsAndLeftBoundaries(chars, heights, leftBoundaries, left);

            // Update right boundaries for each row
            Solution.updateRightBoundaries(chars, rightBoundaries, n);

            // Calculate the maximal rectangle for each row
            maxRectangle = Solution.calculateMaxRectangle(heights, leftBoundaries, rightBoundaries, maxRectangle);
        }

        return maxRectangle;
    }

    /**
     * Updates the heights and left boundaries of rectangles for a given row.
     *
     * @param row            The row in the matrix.
     * @param heights        The array storing the heights of rectangles.
     * @param leftBoundaries The array storing the left boundaries of rectangles.
     * @param left           The left boundary for the current row.
     */
    private static void updateHeightsAndLeftBoundaries(
            final char[] row, final int[] heights, final int[] leftBoundaries, int left) {
        int i = left;
        for (int j = 0; j < heights.length; j++) {
            if ((int) '1' == (int) row[j]) {
                heights[j]++;
                leftBoundaries[j] = Math.max(leftBoundaries[j], i);
            } else {
                heights[j] = 0;
                leftBoundaries[j] = 0;
                i = j + 1;
            }
        }
    }

    /**
     * Updates the right boundaries of rectangles for a given row.
     *
     * @param row             The row in the matrix.
     * @param rightBoundaries The array storing the right boundaries of rectangles.
     * @param right           The right boundary for the current row.
     */
    private static void updateRightBoundaries(final char[] row, final int[] rightBoundaries, int right) {
        int i = right;
        for (int j = rightBoundaries.length - 1; j >= 0; j--) {
            if ((int) '1' == (int) row[j]) {
                rightBoundaries[j] = Math.min(rightBoundaries[j], i);
            } else {
                rightBoundaries[j] = i;
                i = j;
            }
        }
    }

    /**
     * Calculates the maximal rectangle for a given row.
     *
     * @param heights         The array storing the heights of rectangles.
     * @param leftBoundaries  The array storing the left boundaries of rectangles.
     * @param rightBoundaries The array storing the right boundaries of rectangles.
     * @param maxRectangle    The maximal rectangle found so far.
     *
     * @return The maximal rectangle found after considering the current row.
     */
    private static int calculateMaxRectangle(
            final int[] heights, final int[] leftBoundaries, final int[] rightBoundaries, int maxRectangle) {
        int rectangle = maxRectangle;
        for (int j = 0; j < heights.length; j++) {
            final int width = rightBoundaries[j] - leftBoundaries[j];
            final int area = heights[j] * width;
            rectangle = Math.max(rectangle, area);
        }
        return rectangle;
    }
}
