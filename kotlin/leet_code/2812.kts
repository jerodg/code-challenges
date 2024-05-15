/**
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
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
 * This class provides a solution for a specific problem.
 * It contains a method to calculate the maximum safeness factor of a grid.
 */
class Solution {
    // List of possible directions to move in the grid
    private val directions = listOf(
        Pair(1, 0),  // Down
        Pair(-1, 0), // Up
        Pair(0, 1),  // Right
        Pair(0, -1), // Left
    )

    /**
     * This function calculates the maximum safeness factor of a grid.
     *
     * @param grid The grid represented as a list of list of integers.
     * @return The maximum safeness factor as an integer.
     */
    fun maximumSafenessFactor(grid: List<List<Int>>): Int {
        // Convert the grid to a 2D array for easier manipulation
        val arrayGrid = grid.map { it.toIntArray() }.toTypedArray()
        val stack = ArrayDeque<Pair<Int, Int>>()

        // Initialize the grid and stack
        for (i in arrayGrid.indices) {
            for (j in arrayGrid[0].indices) {
                if (arrayGrid[i][j] == 1) {
                    stack.add(Pair(i, j))
                    arrayGrid[i][j] = 0
                } else {
                    arrayGrid[i][j] = -1
                }
            }
        }

        // Calculate the safeness factor for each cell
        var safety = 1
        while (stack.isNotEmpty()) {
            repeat(stack.size) {
                val point = stack.removeLast()
                for (direction in directions) {
                    val x = point.first + direction.first
                    val y = point.second + direction.second

                    if (x < 0 || x > arrayGrid.lastIndex || y < 0 || y > arrayGrid[0].lastIndex || arrayGrid[x][y] != -1) {
                        continue
                    }

                    arrayGrid[x][y] = safety
                    stack.addFirst(Pair(x, y))
                }
            }

            safety++
        }

        // Use a priority queue to find the path with the maximum safeness factor
        val pq = PriorityQueue<PointAndSafeness>(compareBy<PointAndSafeness?> { it!!.safenessFactor }.reversed())
        val start = PointAndSafeness(arrayGrid[0][0], Pair(0, 0))
        pq.add(start)
        arrayGrid[0][0] = -1

        // Process the priority queue until it's empty or the destination is reached
        while (pq.isNotEmpty()) {
            val pointAndSafeness = pq.poll()
            val point = pointAndSafeness.point

            if (point.first == arrayGrid.lastIndex && point.second == arrayGrid[0].lastIndex) {
                return pointAndSafeness.safenessFactor
            }

            for (direction in directions) {
                val x = point.first + direction.first
                val y = point.second + direction.second
                val newPoint = Pair(x, y)

                if (x < 0 || x > arrayGrid.lastIndex || y < 0 || y > arrayGrid[0].lastIndex || arrayGrid[x][y] == -1) {
                    continue
                }

                pq.add(PointAndSafeness(min(pointAndSafeness.safenessFactor, arrayGrid[x][y]), newPoint))
                arrayGrid[x][y] = -1
            }
        }

        // If no path is found, return -1
        return -1
    }
}

/**
 * This data class represents a point in the grid and its safeness factor.
 *
 * @property safenessFactor The safeness factor of the point.
 * @property point The coordinates of the point in the grid.
 */
data class PointAndSafeness(
    val safenessFactor: Int, val point: Pair<Int, Int>
)
