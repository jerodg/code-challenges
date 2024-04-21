/**
 * @file 1971.cpp
 * @brief Contains the implementation of the Solution class.
 *
 * This file contains the implementation of a Solution class which provides a method to check if there is a valid path in a graph.
 */

#include <iosfwd> // For std::ios::sync_with_stdio
#include <iostream> // For std::cin.tie and std::cout.tie
#include <vector> // For std::vector

/**
 * @class Solution
 * @brief A class providing a method to check if there is a valid path in a graph.
 *
 * This class provides a method to check if there is a valid path in a graph. The graph is represented by a list of edges and the method checks if there is a valid path from a source node to a destination node.
 */
class Solution {
    std::vector<int> leader_; ///< The leader of each node in the graph.
    std::vector<int> size_; ///< The size of each node in the graph.

public:
    /**
     * @brief Finds the leader of a node.
     *
     * This method finds the leader of a node in the graph.
     *
     * @param u The node to find the leader of.
     * @return The leader of the node.
     */
    [[nodiscard]] int find(int u) const {
        while (u != leader_[u])
            u = leader_[u];
        return u;
    }

    /**
     * @brief Combines two nodes.
     *
     * This method combines two nodes in the graph.
     *
     * @param u The first node to combine.
     * @param v The second node to combine.
     */
    void combine(int u, int v) {
        u = find(u);
        v = find(v);
        if (u == v)
            return;
        if (size_[u] > size_[v])
            std::swap(u, v);
        leader_[u] = v;
        size_[v] += size_[u];
    }

    /**
     * @brief Checks if there is a valid path in the graph.
     *
     * This method checks if there is a valid path in the graph from a source node to a destination node.
     *
     * @param n The number of nodes in the graph.
     * @param edges The edges in the graph.
     * @param source The source node.
     * @param destination The destination node.
     * @return True if there is a valid path, false otherwise.
     */
    bool validPath(const int n, const std::vector<std::vector<int> > &edges, const int source, const int destination) {
        std::ios::sync_with_stdio(false);
        std::cin.tie(nullptr);
        std::cout.tie(nullptr);
        leader_ = std::vector<int>(n);
        size_ = std::vector<int>(n, 1);
        for (int i = 0; i < n; i++)
            leader_[i] = i;
        for (const auto &edge: edges)
            combine(edge[0], edge[1]);
        return find(source) == find(destination);
    }
};
