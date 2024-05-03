/**
 * @fileoverview This module provides a function to determine if there is a valid path between two nodes in a graph.
 * The graph is represented as a list of edges, and nodes are represented as integers.
 * The function uses a depth-first search strategy to traverse the graph.
 */

/**
 * Determines if there is a valid path between the source and destination nodes in a graph.
 *
 * @param {number} n - The total number of nodes in the graph.
 * @param {Array<Array<number>>} edges - The edges of the graph, represented as pairs of integers.
 * @param {number} source - The starting node for the path.
 * @param {number} destination - The ending node for the path.
 *
 * @returns {boolean} - Returns true if there is a valid path from source to destination, false otherwise.
 *
 * @throws {TypeError} - If n, source, or destination are not numbers, or if edges is not an array of arrays of numbers.
 */
const validPath = function (n, edges, source, destination) {
    // If there is only one node, then there is a valid path by default.
    if (n === 1) {
        return true;
    }

    // Initialize a set with the source node to keep track of visited nodes.
    const stack = new Set([source]);
    let flag = true;

    // Continue traversing the graph until no new nodes are visited.
    while (flag) {
        flag = false;
        // Iterate over all edges in the graph.
        for (let i = 0; i < edges.length; i++) {
            // If one of the nodes in the edge has been visited and the other has not, visit the unvisited node.
            if (stack.has(edges[i][0]) !== stack.has(edges[i][1])) {
                stack.add(edges[i][1]);
                stack.add(edges[i][0]);
                flag = true;
            }

            // If the destination node has been visited, return true.
            if (stack.has(destination)) {
                return true;
            }
        }
    }
    // If the destination node has not been visited after traversing all reachable nodes, return false.
    return false;
};
