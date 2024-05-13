/**
 * Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
 */

/**
 * The `Solution` object encapsulates the solution for a specific problem from LeetCode.
 */
object Solution {
  /**
   * This function calculates the maximum score a binary matrix can have by flipping rows and columns.
   * The score of a binary matrix is the sum of its elements, where each element in the ith row and jth column contributes 2^(n-j-1) to the score, n being the number of columns.
   * The row flips are performed first, each row of the matrix is flipped such that the first element of each row is 1.
   * Then, each column is flipped if the number of 0s is more than the number of 1s in that column.
   *
   * @param grid The input binary matrix.
   * @return The maximum possible score of the binary matrix after flipping.
   */
  def matrixScore(grid: Array[Array[Int]]): Int = {
    // Get the number of rows in the grid
    val rows=grid.length
    // Get the number of columns in the grid
    val columns= grid(0).length
    // Flip the rows of the grid such that the first element of each row is 1
    val toggle=grid.map(row=>   if   (row(0)==0)   row.map(1- _)   else   row)
    // Calculate the maximum possible score of the binary matrix after flipping
    (1 until columns).foldLeft(rows*math.pow(2,columns-1).toInt){(acc,j)=>
      // Count the number of 1s in the jth column
      val cntOnes= toggle.map(_(j)).count(_   ==   1)
      // Add the maximum possible score of the jth column to the total score
      acc+math.max(cntOnes,rows-cntOnes)* math.pow(2,columns-j-1).toInt
    }
  }
}
