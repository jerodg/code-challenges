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

/** The `Solution` object contains methods to solve a specific problem related to finding the maximum safeness factor in
  * a grid.
  */
object Solution {

  /** This method calculates the maximum safeness factor in a grid.
    *
    * @param grid
    *   The grid represented as a list of lists of integers.
    * @return
    *   The maximum safeness factor as an integer.
    */
  def maximumSafenessFactor(grid: List[List[Int]]): Int = {
    val last = grid.length - 1
    if (grid(0)(0) == 1 || grid(last)(last) == 1) 0
    else {
      val ga           = grid.map(_.toArray).toArray
      val factors      = Array.ofDim[Int](last + 1, last + 1)
      val firstPairSet = Set((0, 0))
      val lastPair     = (last, last)

      /** This method collects the neighbours of a given cell in the grid.
        *
        * @param i
        *   The row index of the cell.
        * @param j
        *   The column index of the cell.
        * @return
        *   A sequence of tuples representing the neighbours of the cell.
        */
      def collectNeighbours(i: Int, j: Int): Seq[(Int, Int)] = {
        val all = Seq((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
        if (0 < i && i < last && 0 < j && j < last) all
        else all.filter(p => 0 <= p._1 && p._1 <= last && 0 <= p._2 && p._2 <= last)
      }

      val neighbours = Array.tabulate(last + 1, last + 1)(collectNeighbours)

      /** This method marks the factors in the grid using Breadth-First Search (BFS).
        *
        * @param edge
        *   The set of cells to start the BFS from.
        * @param passed
        *   The set of cells that have already been visited.
        * @param nextFactor
        *   The next factor to be marked.
        */
      @annotation.tailrec
      def markFactorsBFS(edge: Set[(Int, Int)], passed: Set[(Int, Int)] = Set.empty, nextFactor: Int = 1): Unit =
        if (edge.nonEmpty) {
          val nextPassed = passed ++ edge
          val nextEdge   = edge.flatMap(p => neighbours(p._1)(p._2)) -- nextPassed
          nextEdge.foreach(p => factors(p._1)(p._2) = nextFactor)
          markFactorsBFS(nextEdge, nextPassed, nextFactor + 1)
        }

      /** This method checks if a safe path exists in the grid using BFS.
        *
        * @param safeness
        *   The safeness factor to check for.
        * @param edge
        *   The set of cells to start the BFS from.
        * @param passed
        *   The set of cells that have already been visited.
        * @return
        *   A boolean indicating whether a safe path exists or not.
        */
      @annotation.tailrec
      def safePathExistsBFS(
          safeness: Int,
          edge: Set[(Int, Int)] = firstPairSet,
          passed: Set[(Int, Int)] = Set.empty
      ): Boolean =
        if (edge.isEmpty) false
        else if (edge.contains(lastPair)) true
        else {
          val nextPassed = passed ++ edge
          val nextEdge   = edge.flatMap(p => neighbours(p._1)(p._2)) -- nextPassed
          safePathExistsBFS(safeness, nextEdge.filter(p => factors(p._1)(p._2) >= safeness), nextPassed)
        }

      /** This method finds the maximum safeness factor using Binary Search (BS).
        *
        * @param first
        *   The first factor to start the BS from.
        * @param end
        *   The last factor to end the BS at.
        * @return
        *   The maximum safeness factor as an integer.
        */
      @annotation.tailrec
      def maxSafenessBS(first: Int, end: Int): Int = {
        val delta    = end - first
        lazy val mid = first + delta / 2
        if (delta <= 1) first
        else if (safePathExistsBFS(mid))
          maxSafenessBS(mid, end)
        else
          maxSafenessBS(first, mid)
      }

      val thieves = (for (i <- 0 to last; j <- 0 to last if ga(i)(j) == 1) yield (i, j)).toSet
      markFactorsBFS(thieves)
      val maxSafeness = factors(0)(0).min(factors(last)(last))
      if (safePathExistsBFS(maxSafeness)) maxSafeness
      else maxSafenessBS(0, maxSafeness)
    }
  }
}
