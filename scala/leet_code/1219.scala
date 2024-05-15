/** Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
  *
  * This program is free software: you can redistribute it and/or modify it under the terms of the Server Side Public
  * License (SSPL) as published by MongoDB, Inc., either version 1 of the License, or (at your option) any later
  * version.
  *
  * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
  * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL for more details.
  *
  * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
  * Software. You should have received a copy of the SSPL along with this program. If not, see <a
  * href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
  */

/** The `Solution` object contains methods to solve a specific problem related to finding the maximum gold in a grid.
  */
object Solution {

  /** A 2D array representing the four possible directions (up, down, left, right) in the grid.
    */
  private val dirs = Array(Array(1, 0), Array(0, 1), Array(-1, 0), Array(0, -1))

  /** This method calculates the maximum amount of gold that can be collected in the grid.
    *
    * @param grid
    *   The grid represented as a 2D array of integers, where each integer represents the amount of gold in a cell.
    * @return
    *   The maximum amount of gold that can be collected as an integer.
    */
  def getMaximumGold(grid: Array[Array[Int]]): Int = {
    var res = 0
    grid.indices.foreach(i => grid(0).indices.foreach(j => if (grid(i)(j) > 0) res = res.max(dfs(grid, i, j))))
    res
  }

  /** This method performs a Depth-First Search (DFS) on the grid from a given cell and calculates the amount of gold
    * that can be collected.
    *
    * @param grid
    *   The grid represented as a 2D array of integers.
    * @param i
    *   The row index of the starting cell.
    * @param j
    *   The column index of the starting cell.
    * @return
    *   The amount of gold that can be collected from the starting cell as an integer.
    */
  def dfs(grid: Array[Array[Int]], i: Int, j: Int): Int = {
    if (i < 0 || i >= grid.length || j < 0 || j >= grid(0).length || grid(i)(j) == 0) return 0
    val v = grid(i)(j)
    grid(i)(j) = 0
    var res = 0

    dirs.foreach(arr => {
      val r = i + arr(0)
      val c = j + arr(1)
      res = res.max(v + dfs(grid, r, c))
    })

    grid(i)(j) = v
    res
  }
}
