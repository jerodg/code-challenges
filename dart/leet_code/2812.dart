/// Copyright ©2010-2024 JerodG <https://github.com/jerodg/>
///
/// This program is free software: you can redistribute it and/or modify it under the terms of the
/// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
/// or (at your option) any later version.
///
/// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
/// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
/// for more details.
///
/// The above copyright notice and this permission notice shall be included in all copies or
/// substantial portions of the Software. You should have received a copy of the SSPL along with this
/// program. If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
///
/// This file `leet_code/2812.dart` contains a solution for calculating the maximum safeness factor in a grid.
/// It uses a breadth-first search algorithm to find the shortest distance from each cell to the nearest obstacle,
/// and a priority queue to find the path with the maximum safeness factor.
library;

import 'dart:collection';

import 'package:collection/collection.dart' show PriorityQueue;

/// A `Solution` class.
///
/// This class provides a method to calculate the maximum safeness factor in a grid.
class Solution {
  /// Calculates the maximum safeness factor in a grid.
  ///
  /// The method takes a 2D grid as input and returns the maximum safeness factor.
  /// If no path is found, it returns -1.
  ///
  /// The [grid] parameter is a 2D list of integers where 1 represents an obstacle and 0 represents a free cell.
  ///
  /// Returns an integer representing the maximum safeness factor.
  int maximumSafenessFactor(List<List<int>> grid) {
    // The number of rows in the grid
    int n = grid.length;
    // The number of columns in the grid
    int m = grid[0].length;
    // The four possible directions to move in the grid
    List<List<int>> directions = [
      [0, 1], // right
      [1, 0], // down
      [0, -1], // left
      [-1, 0] // up
    ];
    // The distance from each cell to the nearest obstacle
    List<List<int>> distance = List.generate(n, (_) => List.filled(m, n * m));
    // A queue for the breadth-first search
    Queue<List<int>> queue = Queue();

    // Initialize the distance and queue with the obstacles
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        if (grid[i][j] == 1) {
          queue.add([i, j]);
          distance[i][j] = 0;
        }
      }
    }

    // Perform the breadth-first search
    while (queue.isNotEmpty) {
      var cell = queue.removeFirst();
      int x = cell[0], y = cell[1];
      for (var dir in directions) {
        int nx = x + dir[0], ny = y + dir[1];
        if (nx >= 0 && ny >= 0 && nx < n && ny < m && distance[nx][ny] > distance[x][y] + 1) {
          distance[nx][ny] = distance[x][y] + 1;
          queue.add([nx, ny]);
        }
      }
    }

    // A priority queue for finding the path with the maximum safeness factor
    PriorityQueue<List<int>> pq = PriorityQueue((a, b) => b[2].compareTo(a[2]));
    pq.add([0, 0, distance[0][0]]);
    // A set for keeping track of the visited cells
    Set<String> visited = {};

    // Find the path with the maximum safeness factor
    while (pq.isNotEmpty) {
      var cell = pq.removeFirst();
      int x = cell[0], y = cell[1], safeness = cell[2];
      if (x == n - 1 && y == m - 1) {
        return safeness;
      }
      String key = "$x,$y";
      if (visited.contains(key)) continue;
      visited.add(key);
      for (var dir in directions) {
        int nx = x + dir[0], ny = y + dir[1];
        if (nx >= 0 && ny >= 0 && nx < n && ny < m && !visited.contains("$nx,$ny")) {
          pq.add([nx, ny, safeness.clamp(0, distance[nx][ny])]);
        }
      }
    }

    // If no path is found, return -1
    return -1;
  }
}
