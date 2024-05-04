/**
 * This module is part of a leet code solution. It contains a single class, Solution, which
 * provides a method to calculate the minimum falling path sum in a given grid.
 * The method uses dynamic programming to solve the problem.
 */
class Solution {

    /**
     * This method calculates the minimum falling path sum in a given grid.
     *
     * @param grid The input grid. It is expected to be a non-null 2D integer array.
     *
     * @return The minimum falling path sum. The return type is an integer.
     */
    public int minFallingPathSum(final int[][] grid) {
        final int n = grid.length;
        return this.minFallingPathSum(0, grid).minSum;
    }

    /**
     * This method calculates the minimum falling path sum for a given row in the grid.
     * It uses recursion and dynamic programming to solve the problem.
     *
     * @param row  The row in the grid to start the calculation from. It is expected to be an integer.
     * @param grid The input grid. It is expected to be a non-null 2D integer array.
     *
     * @return A Triplet object containing the minimum sum, the second minimum sum, and the index of the minimum sum.
     */
    private Triplet minFallingPathSum(final int row, final int[][] grid) {

        if (row == grid.length) {
            return new Triplet(0, 0, 0);
        }

        final Triplet nextRowTriplet = this.minFallingPathSum(row + 1, grid); //trying passing row++
        final Triplet currentTriplet = new Triplet(Integer.MAX_VALUE, Integer.MAX_VALUE, -1);

        for (int col = 0; col < grid[0].length; col++) {
            final int sum = grid[row][col] + ((col == nextRowTriplet.minSumIndex) ? nextRowTriplet.secondMinSum : nextRowTriplet.minSum);
            if (sum <= currentTriplet.minSum) {
                currentTriplet.secondMinSum = currentTriplet.minSum;
                currentTriplet.minSum = sum;
                currentTriplet.minSumIndex = col;
            } else if (sum < currentTriplet.secondMinSum) {
                currentTriplet.secondMinSum = sum;
            }
        }

        return currentTriplet;
    }
}

/**
 * This class represents a triplet of integers. It is used to store the minimum sum, the second minimum sum,
 * and the index of the minimum sum in the grid.
 */
class Triplet {
    int minSum;
    int secondMinSum;
    int minSumIndex;

    /**
     * This constructor initializes a new Triplet object with the given values.
     *
     * @param minSum       The minimum sum. It is expected to be an integer.
     * @param secondMinSum The second minimum sum. It is expected to be an integer.
     * @param minSumIndex  The index of the minimum sum. It is expected to be an integer.
     */
    Triplet(int minSum, int secondMinSum, int minSumIndex) {
        this.minSum = minSum;
        this.secondMinSum = secondMinSum;
        this.minSumIndex = minSumIndex;
    }
}
