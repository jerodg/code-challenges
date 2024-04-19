/** This object provides a solution for the problem of counting the number of islands in a 2D grid.
  * An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
  * You may assume all four edges of the grid are all surrounded by water.
  *
  * @example
  * {{{
  * val grid = Array(
  *   Array('1','1','1','1','0'),
  *   Array('1','1','0','1','0'),
  *   Array('1','1','0','0','0'),
  *   Array('0','0','0','0','0')
  * )
  * assert(numIslands(grid) == 1)
  * }}}
  */
object Solution {

  /** This function counts the number of islands in a 2D grid.
    *
    * @param grid A 2D array representing the grid. '1' represents land and '0' represents water.
    * @return The number of islands in the grid.
    */
  def numIslands(grid: Array[Array[Char]]): Int = {
    val directions = Array(Array(-1, 0), Array(1, 0), Array(0, -1), Array(0, 1))

    /** This function checks if a given cell (i, j) is valid, i.e., it is inside the grid.
      *
      * @param i The row index of the cell.
      * @param j The column index of the cell.
      * @return True if the cell is inside the grid, false otherwise.
      */
    def isValid(i: Int, j: Int): Boolean = {
      i >= 0 && i < grid.length && j >= 0 && j < grid(i).length
    }

    /** This function performs a Depth-First Search (DFS) from a given cell (i, j).
      *
      * @param i The row index of the cell.
      * @param j The column index of the cell.
      */
    def dfs(i: Int, j: Int): Unit = {
      if (grid(i)(j) == '1') {
        grid(i)(j) = '0'
        for (direction <- directions) {
          val newI = i + direction(0)
          val newJ = j + direction(1)
          if (isValid(newI, newJ)) {
            dfs(newI, newJ)
          }
        }
      }
    }

    var count = 0
    for (i <- grid.indices) {
      for (j <- grid(i).indices) {
        if (grid(i)(j) == '1') {
          count += 1
          dfs(i, j)
        }
      }
    }
    count
  }
}
