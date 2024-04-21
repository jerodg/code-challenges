#include <stdlib.h>  // Required for dynamic memory allocation functions

/**
 * @file leet_code/1971.c
 * @brief This file contains the implementation of the validPath function.
 *
 * The function checks if there is a valid path between the source and destination nodes in a graph.
 * The graph is represented as an adjacency list.
 */

/**
 * @brief Checks if there is a valid path between the source and destination nodes in a graph.
 *
 * This function uses a breadth-first search algorithm to traverse the graph.
 * It starts from the source node and visits all its adjacent nodes.
 * If it reaches the destination node during the traversal, it returns true.
 * If it has visited all nodes and hasn't reached the destination node, it returns false.
 *
 * @param n Number of nodes in the graph.
 * @param edges 2D array representing the edges of the graph.
 * @param edgesSize Number of edges in the graph.
 * @param edgesColSize Array representing the number of columns in each row of the edges array.
 * @param source The source node.
 * @param destination The destination node.
 * @return True if there is a valid path from source to destination, false otherwise.
 */
bool validPath(int n, int **edges, int edgesSize, int *edgesColSize, int source, int destination) {
    if (source == destination) {
        return true;
    }

    bool *visited = calloc(n, sizeof(bool));
    visited[source] = true;
    bool updated;
    do {
        updated = false;
        for (int i = 0; i < edgesSize; i++) {
            if (visited[edges[i][0]] ^ visited[edges[i][1]]) {
                // only one side of edge visited
                updated = true;
                if (edges[i][0] == destination || edges[i][1] == destination) {
                    // got to destination
                    free(visited);
                    return true;
                }
                if (visited[edges[i][0]]) {
                    visited[edges[i][1]] = true;
                } else {
                    visited[edges[i][0]] = true;
                }
            }
        }
    } while (updated);
    free(visited);
    return false;
}
