/** This object represents a solution for finding the minimum falling path sum in a grid.
  * A falling path starts at any element in the first row and chooses the element in the next row which is either directly below or diagonally below to the left or right.
  * The goal is to reach the last row with the minimum sum of the chosen path.
  */
object Solution {

  /** Finds the minimum falling path sum in a grid.
    *
    * This method iterates over the grid, updating the sumRow array with the minimum sum of the falling path up to the current row.
    * It uses a helper function to find the indices of the minimum and the second minimum elements in the sumRow array.
    * It then updates the current row by adding the minimum sum of the falling path that ends at each element.
    *
    * @param grid The input grid. It should be a 2D array of integers.
    * @return The minimum falling path sum in the grid. It returns an integer.
    */
  def minFallingPathSum(grid: Array[Array[Int]]): Int = if (grid.length == 1)
    grid.head.head
  else {

    /** Finds the indices of the minimum and the second minimum elements in a row.
      *
      * This method iterates over the row, keeping track of the indices of the minimum and the second minimum elements.
      *
      * @param row The input row. It should be an array of integers.
      * @return A tuple of two integers representing the indices of the minimum and the second minimum elements in the row.
      */
    def findMinInds(row: Array[Int]): (Int, Int) =
      row.indices.foldLeft((0, 1)) {
        case ((minInd, nextMinInd), i) if row(i) < row(minInd) => (i, minInd)
        case ((minInd, nextMinInd), i)
            if row(i) < row(nextMinInd) && i != minInd =>
          (minInd, i)
        case (mins, _) => mins
      }

    grid.reduceLeft { (sumRow, row) =>
      val (minInd, nextMinInd) = findMinInds(sumRow)
      val min = sumRow(minInd)
      for (i <- row.indices)
        row(i) += (if (i != minInd) min else sumRow(nextMinInd))
      row
    }.min
  }
}
