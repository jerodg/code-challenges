/// <summary>
/// This class provides a solution for the problem of checking if there is a valid path in a graph.
/// A path in a graph is a sequence of vertices where each pair of adjacent vertices is connected by an edge.
/// </summary>
public class Solution
{
    /// <summary>
    /// This method checks if there is a valid path between the source and destination vertices in the graph.
    /// </summary>
    /// <param name="n">The number of vertices in the graph.</param>
    /// <param name="edges">An array of edge pairs where each pair is an edge connecting two vertices in the graph.</param>
    /// <param name="source">The source vertex.</param>
    /// <param name="destination">The destination vertex.</param>
    /// <returns>True if there is a valid path from source to destination, false otherwise.</returns>
    public bool ValidPath(int n, int[][] edges, int source, int destination)
    {
        int[] parent = new int[n]; // An array to store the parent of each vertex in the graph.

        // Initialize each vertex to be its own parent.
        for (int i = 0; i < n; i++)
            parent[i] = i;

        // For each edge in the graph, find the parents of the two vertices and if they are not the same, union them.
        foreach (var edge in edges)
        {
            int parent1 = FindParent(parent, edge[0]);
            int parent2 = FindParent(parent, edge[1]);
            if (parent1 != parent2)
                parent[parent2] = parent1;
        }

        // Check if the source and destination vertices are in the same connected component of the graph.
        return FindParent(parent, source) == FindParent(parent, destination);
    }

    /// <summary>
    /// This method finds the parent of a vertex in the graph using path compression technique.
    /// </summary>
    /// <param name="parent">An array where the index is a vertex and the value at the index is the parent of the vertex.</param>
    /// <param name="node">The vertex whose parent is to be found.</param>
    /// <returns>The parent of the vertex.</returns>
    private int FindParent(int[] parent, int node)
    {
        // If the parent of the vertex is not itself, recursively find the parent.
        if (parent[node] != node)
            parent[node] = FindParent(parent, parent[node]);

        return parent[node]; // Return the parent of the vertex.
    }
}
