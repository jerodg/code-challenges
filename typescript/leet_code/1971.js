/**
 * @fileoverview This module provides a function to check if there is a valid path between two nodes in a graph.
 * @module leet_code/1971
 */
/**
 * Function to check if there is a valid path between two nodes in a graph.
 * The graph is represented as an adjacency list, and the nodes are numbered from 0 to n-1.
 * The function uses a depth-first search approach to traverse the graph.
 *
 * @param {number} n - The number of nodes in the graph.
 * @param {number[][]} edges - The edges of the graph, represented as an array of pairs of nodes.
 * @param {number} source - The source node.
 * @param {number} destination - The destination node.
 * @returns {boolean} - Returns true if there is a valid path from the source to the destination, false otherwise.
 * @throws {Error} - Throws an error if the input parameters are not valid.
 */
function validPath(n, edges, source, destination) {
    var _a, _b;
    // Check if the input parameters are valid
    if (n < 0 || !Array.isArray(edges) || typeof source !== 'number' || typeof destination !== 'number') {
        throw new Error('Invalid input parameters');
    }
    // If there is only one node and no edges, and the source is node 0, then there is a valid path
    if (1 === n && !edges.length && 0 === source) {
        return true;
    }
    // Initialize the hash maps for the source and destination nodes
    var sourceHm = (_a = {}, _a[source] = true, _a);
    var destHm = (_b = {}, _b[destination] = true, _b);
    // Check if there is a direct edge between the source and destination nodes
    var isConnected = edges.some(function (pair) {
        // If the first node of the pair is the source, mark the second node as visited from the source
        if (sourceHm[pair[0]]) {
            sourceHm[pair[1]] = true;
        }
        // If the second node of the pair is the source, mark the first node as visited from the source
        else if (sourceHm[pair[1]]) {
            sourceHm[pair[0]] = true;
        }
        // If the first node of the pair is the destination, mark the second node as visited from the destination
        if (destHm[pair[0]]) {
            destHm[pair[1]] = true;
        }
        // If the second node of the pair is the destination, mark the first node as visited from the destination
        else if (destHm[pair[1]]) {
            destHm[pair[0]] = true;
        }
        // If both the source and destination nodes have visited the same node, then there is a valid path
        return sourceHm[pair[0]] && destHm[pair[0]];
    });
    // If there is a direct edge between the source and destination nodes, return true
    if (isConnected) {
        return true;
    }
    // If there is no direct edge, check if there is an indirect path by traversing the graph
    return edges.some(function (pair) {
        // The logic is the same as above
        if (sourceHm[pair[0]]) {
            sourceHm[pair[1]] = true;
        } else if (sourceHm[pair[1]]) {
            sourceHm[pair[0]] = true;
        }
        if (destHm[pair[0]]) {
            destHm[pair[1]] = true;
        } else if (destHm[pair[1]]) {
            destHm[pair[0]] = true;
        }
        return sourceHm[pair[0]] && destHm[pair[0]];
    });
}
