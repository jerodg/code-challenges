import scala.collection.mutable.ArrayBuffer

/** This is the Solution object. It contains a method to calculate the perimeter of an island in a given 2D array. Each
  * cell in the 2D array represents a piece of land, where 1 represents land and 0 represents water. The method returns
  * an integer representing the total perimeter of the island.
  *
  * @example
  *   val grid = Array(Array(0,1,0,0), Array(1,1,1,0), Array(0,1,0,0), Array(1,1,0,0)) val result =
  *   Solution.islandPerimeter(grid) // result: 16
  *
  * @note
  *   The method does not modify the input array.
  */
object Solution {

  /** Calculates the perimeter of an island in the given 2D array.
    *
    * @param grid
    *   A 2D array representing the grid. Each cell represents a piece of land, where 1 represents land and 0 represents
    *   water.
    * @return
    *   An integer representing the total perimeter of the island.
    * @throws IllegalArgumentException
    *   if the input array is empty or not rectangular.
    */
  def islandPerimeter(grid: Array[Array[Int]]): Int = {
    // Check if the input array is empty or not rectangular
    if (grid.isEmpty || grid.exists(_.length != grid(0).length)) {
      throw new IllegalArgumentException(
        "Input array must be non-empty and rectangular"
      )
    }

    // Helper function to count the perimeter of a land cell
    def countPerimeter(i: Int, j: Int): Int = {
      var perimeter: Int = 4
      if (i - 1 >= 0 && grid(i - 1)(j) == 1) perimeter -= 1
      if (i + 1 < grid.length && grid(i + 1)(j) == 1) perimeter -= 1
      if (j - 1 >= 0 && grid(i)(j - 1) == 1) perimeter -= 1
      if (j + 1 < grid(i).length && grid(i)(j + 1) == 1) perimeter -= 1
      perimeter
    }

    var totalPerimeter: Int = 0

    // Iterate over each cell in the array
    for (i <- grid.indices) {
      for (j <- grid(i).indices) {
        // If the cell represents land
        if (grid(i)(j) == 1) {
          // Add the perimeter of the land cell to the total perimeter
          totalPerimeter += countPerimeter(i, j)
        }
      }
    }

    // Return the total perimeter
    totalPerimeter
  }
}
