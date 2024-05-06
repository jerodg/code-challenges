import scala.collection.mutable.Stack

/** This object contains solutions for two problems related to finding the largest rectangle in a matrix. The first
  * function, largestRectangleArea, finds the largest rectangle that can be formed using the given heights. The second
  * function, maximalRectangle, finds the largest rectangle that can be formed in a given matrix.
  */
object Solution {

  /** This function calculates the largest rectangle that can be formed in a given matrix. It uses the
    * largestRectangleArea function to calculate the largest rectangle for each row of the matrix.
    *
    * @param matrix
    *   A 2D array of characters representing the matrix.
    * @return
    *   The area of the largest rectangle that can be formed in the given matrix.
    */
  def maximalRectangle(matrix: Array[Array[Char]]): Int = {
    if (matrix.isEmpty) return 0
    val m: Int              = matrix.length
    val n: Int              = matrix(0).length
    val heights: Array[Int] = Array.fill(n)(0)
    var maxArea: Int        = 0
    for (i <- 0 until m) {
      for (j <- 0 until n) {
        if (matrix(i)(j) == '1') {
          heights(j) += 1
        } else {
          heights(j) = 0
        }
      }
      maxArea = maxArea max largestRectangleArea(heights)
    }
    maxArea
  }

  /** This function calculates the largest rectangle that can be formed using the given heights. It uses a stack to keep
    * track of the indices of the heights.
    *
    * @param heights
    *   An array of integers representing the heights.
    * @return
    *   The area of the largest rectangle that can be formed using the given heights.
    */
  def largestRectangleArea(heights: Array[Int]): Int = {
    val n: Int            = heights.length
    val left: Array[Int]  = Array.fill(n)(0)
    val right: Array[Int] = Array.fill(n)(n)
    val stack: Stack[Int] = Stack[Int]()
    for (i <- 0 until n) {
      while (stack.nonEmpty && heights(stack.top) >= heights(i)) {
        right(stack.top) = i
        stack.pop()
      }
      left(i) = if (stack.isEmpty) -1 else stack.top
      stack.push(i)
    }
    var maxArea: Int = 0
    for (i <- 0 until n) {
      maxArea = maxArea max (right(i) - left(i) - 1) * heights(i)
    }
    maxArea
  }
}
