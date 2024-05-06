/** This object represents a solution for checking if there is a valid path between two nodes in a graph. The graph is
  * represented as an undirected graph with n nodes, where each node is numbered between 0 and n - 1. The edges are
  * represented as a 2D array, where each edge connects two nodes. A path is valid if it starts from the source node and
  * ends at the destination node. The path should also be connected, which means there is an edge between each pair of
  * adjacent nodes in the path.
  */
object Solution {

  /** Checks if there is a valid path between two nodes in a graph.
    *
    * This method uses the union-find algorithm to group the nodes into connected components. It then checks if the
    * source node and the destination node are in the same connected component.
    *
    * @param n
    *   The number of nodes in the graph. It should be a positive integer.
    * @param edges
    *   The edges of the graph. It should be a 2D array of integers, where each edge is represented as a 2-element
    *   array.
    * @param source
    *   The source node. It should be an integer between 0 and n - 1.
    * @param destination
    *   The destination node. It should be an integer between 0 and n - 1.
    * @return
    *   A boolean indicating whether there is a valid path between the source node and the destination node. It returns
    *   true if there is a valid path, and false otherwise.
    */
  def validPath(
      n: Int,
      edges: Array[Array[Int]],
      source: Int,
      destination: Int
  ): Boolean = {
    // Initialize the parent array for the union-find algorithm
    val sets = (0 until n).toArray
    // Initialize the rank array for the union-find algorithm
    val rank = Array.fill(n)(0)

    // Define the find operation for the union-find algorithm
    def find(i: Int): Int = {
      if (sets(i) != i) {
        sets(i) = find(sets(i))
      }
      sets(i)
    }

    // Define the union operation for the union-find algorithm
    def union(i: Int, j: Int): Unit = {
      val iset = find(i)
      val jset = find(j)
      if (iset != jset) {
        if (rank(iset) < rank(jset)) {
          sets(iset) = jset
        } else {
          if (rank(iset) == rank(jset)) rank(iset) += 1
          sets(jset) = iset
        }
      }
    }

    // Perform the union operation for each edge
    for (i <- edges.indices) {
      union(edges(i)(0), edges(i)(1))
    }

    // Check if the source node and the destination node are in the same connected component
    find(source) == find(destination)
  }
}
