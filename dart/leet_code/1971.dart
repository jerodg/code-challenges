/// Dart implementation of the LeetCode problem 1971: Find if Path Exists in Graph.
///
/// This module contains a class `Solution` with a method `validPath`.
/// The `validPath` method takes in four parameters:
/// - `n`: An integer representing the number of nodes in the graph.
/// - `edges`: A list of lists where each list contains two integers representing an edge between two nodes.
/// - `source`: An integer representing the source node.
/// - `destination`: An integer representing the destination node.
///
/// The method returns a boolean value indicating whether there is a valid path from the source node to the destination node.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `n` is a positive integer, `edges` is a list of lists with two integers each, and `source` and `destination` are valid node indices.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.

import 'dart:collection';

class Solution {
  /// Checks if there is a valid path from the source node to the destination node in the graph.
  ///
  /// The graph is represented as an adjacency list, which is a list of lists. Each list represents the nodes that the current node is connected to.
  /// The method uses a queue to perform a breadth-first search (BFS) on the graph from the source node.
  /// If the destination node is reached during the BFS, the method returns true. Otherwise, it returns false.
  ///
  /// @param n The number of nodes in the graph.
  /// @param edges The edges of the graph.
  /// @param source The source node.
  /// @param destination The destination node.
  /// @return A boolean value indicating whether there is a valid path from the source node to the destination node.
  bool validPath(int n, List<List<int>> edges, int source, int destination) {
    // Initialize the adjacency list.
    List<List<int>> graph = List.generate(n + 1, (_) => []);

    // Populate the adjacency list with the edges.
    for (int i = 0; i < edges.length; i++) {
      graph[edges[i][0]].add(edges[i][1]);
      graph[edges[i][1]].add(edges[i][0]);
    }

    // Initialize the queue with the source node.
    Queue<int> q = Queue();
    q.add(source);

    // If the source node is the same as the destination node, the path exists.
    bool ans = destination == source;

    // Perform BFS on the graph.
    while (q.length != 0) {
      int sz = q.length;
      for (int i = 0; i < sz; i++) {
        // If the last node in the queue is the destination node, the path exists.
        if (q.last == destination) ans = true;

        // Add all the nodes connected to the last node in the queue to the front of the queue.
        for (int j = 0; j < graph[q.last].length; j++) {
          q.addFirst(graph[q.last][j]);
        }

        // Remove the last node from the queue.
        graph[q.last] = [];
        q.removeLast();
      }
    }

    // Return whether the path exists.
    return ans;
  }
}
