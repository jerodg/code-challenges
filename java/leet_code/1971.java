/**
 * This class provides a solution for determining if there is a valid path between two nodes in a graph.
 * The graph is represented as an adjacency list where each edge is an array of two integers.
 * The nodes are numbered from 0 to n-1.
 */
class Solution {

    /**
     * Determines if there is a valid path between the source and destination nodes in the graph.
     *
     * @param n           The number of nodes in the graph.
     * @param edges       The edges of the graph, where each edge is represented as an array of two integers.
     * @param source      The starting node for the path.
     * @param destination The ending node for the path.
     *
     * @return true if there is a valid path from source to destination, false otherwise.
     *
     * @throws IllegalArgumentException if the source or destination is not a valid node.
     */
    public static boolean validPath(int n, final int[][] edges, final int source, final int destination) {
        // Check if the graph is empty. If it is, return true as there are no obstacles to the path.
        if (edges.length == 0) return true;

        // Initialize an array to keep track of visited nodes.
        final boolean[] visited = new boolean[n];

        // Flag to indicate if any node was visited in the current iteration.
        boolean flag = true;

        // Mark the source node as visited.
        visited[source] = true;

        // Continue visiting nodes until no new node is visited.
        while (flag) {
            flag = false;

            // Visit each edge in the graph.
            for (final int[] edge : edges) {
                // If one node of the edge is visited and the other is not, visit the unvisited node.
                if (visited[edge[0]] != visited[edge[1]]) {
                    visited[edge[0]] = true;
                    visited[edge[1]] = true;
                    flag = true;
                }

                // If the destination node is visited, return true.
                if (visited[destination]) return true;
            }
        }

        // If the destination node is not visited after visiting all reachable nodes, return false.
        return false;
    }
}
