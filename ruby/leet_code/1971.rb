# Function to check if there is a valid path between two nodes in a graph
#
# This function checks if there is a valid path between the source and destination nodes in a graph.
# The graph is represented as an adjacency list, and a path is considered valid if it connects the source and destination nodes.
#
# @param n [Integer] The number of nodes in the graph
# @param edges [Array<Array<Integer>>] The edges of the graph, where each edge is represented as a pair of nodes
# @param source [Integer] The source node
# @param destination [Integer] The destination node
# @return [Boolean] True if there is a valid path, false otherwise
#
# @example
#   valid_path(3, [[0,1],[1,2],[2,0]], 0, 2) #=> true
#
def valid_path(n, edges, source, destination)
  return true if source == destination

  Graph.new(n, edges).solve(source, destination)
end

# Class Graph
#
# This class represents a graph as an adjacency list. It includes methods for solving the problem of finding a valid path between two nodes.
#
class Graph
  attr_reader :adj, :visited, :queue1, :queue2

  # Initialize a new instance of the Graph class
  #
  # @param n [Integer] The number of nodes in the graph
  # @param edges [Array<Array<Integer>>] The edges of the graph, where each edge is represented as a pair of nodes
  #
  def initialize(n, edges)
    @adj = Array.new(n) { [] }
    edges.each do |(x, y)|
      adj[x] << y
      adj[y] << x
    end
    @queue1 = []
    @queue2 = []
  end

  # Function to solve the problem of finding a valid path between two nodes
  #
  # @param source [Integer] The source node
  # @param destination [Integer] The destination node
  # @return [Boolean] True if there is a valid path, false otherwise
  #
  def solve(source, destination)
    @visited = { source => 0, destination => 1 }
    while source && destination
      source = explore(source, 0, 1, queue1)
      return true if source == -1
      destination = explore(destination, 1, 0, queue2)
      return true if destination == -1
    end

    false
  end

  # Function to explore the graph from a given node
  #
  # @param node [Integer] The current node
  # @param current_label [Integer] The label for the current node
  # @param next_label [Integer] The label for the next node
  # @param queue [Array<Integer>] The queue of nodes to be explored
  # @return [Integer, nil] The next node to be explored, or nil if there are no more nodes to be explored
  #
  def explore(node, current_label, next_label, queue)
    adj[node].each do |next_node|
      return -1 if visited[next_node] == next_label
      next if visited[next_node]
      visited[next_node] = current_label
      queue << next_node
    end

    queue.shift
  end
end