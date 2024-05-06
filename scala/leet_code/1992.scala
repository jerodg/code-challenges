/** This is the Solution object. It contains a method to find farmland in a given 2D array. Each cell in the 2D array
  * represents a piece of land, where 1 represents farmland and 0 represents non-farmland. The method returns a 2D array
  * where each sub-array is a rectangle representing a piece of farmland. The rectangle is represented by the
  * coordinates of its upper-left and lower-right corners.
  *
  * @example
  *   val land = Array(Array(1,0,0), Array(0,1,1), Array(0,1,1)) val result = Solution.findFarmland(land) // result:
  *   Array(Array(0,0,0,0), Array(1,1,2,2))
  *
  * @note
  *   The method modifies the input array by setting all farmland cells to 0 after processing them.
  */
object Solution {

  /** Finds all pieces of farmland in the given 2D array.
    *
    * @param land
    *   A 2D array representing the land. Each cell represents a piece of land, where 1 represents farmland and 0
    *   represents non-farmland.
    * @return
    *   A 2D array where each sub-array is a rectangle representing a piece of farmland. The rectangle is represented by
    *   the coordinates of its upper-left and lower-right corners.
    * @throws IllegalArgumentException
    *   if the input array is empty or not rectangular.
    */
  def findFarmland(land: Array[Array[Int]]): Array[Array[Int]] = {
    // Check if the input array is empty or not rectangular
    if (land.isEmpty || land.exists(_.length != land(0).length)) {
      throw new IllegalArgumentException("Input array must be non-empty and rectangular")
    }

    val m   = land.length
    val n   = land(0).length
    val res = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]

    // Iterate over each cell in the array
    for (i <- 0 until m) {
      for (j <- 0 until n) {
        // If the cell represents farmland
        if (land(i)(j) == 1) {
          var x = i
          var y = j
          // Find the lower-right corner of the farmland
          while (x < m && land(x)(j) == 1) {
            x += 1
          }
          while (y < n && land(i)(y) == 1) {
            y += 1
          }
          // Add the farmland to the result
          res += Array(i, j, x - 1, y - 1)
          // Set all cells of the farmland to 0
          for (a <- i until x) {
            for (b <- j until y) {
              land(a)(b) = 0
            }
          }
        }
      }
    }

    // Return the result as an array
    res.toArray
  }
}
