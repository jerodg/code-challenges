// Package leet_code provides solutions for LeetCode problems.
package leet_code

// disjointSet represents a disjoint-set data structure, also known as a union-find data structure or merge-find set.
// It provides operations for adding new sets, merging sets (replacing them by their union), and finding a representative member of a set.
// The ranks array is used to optimize the union operation.
type disjointSet struct {
	roots []int // roots array represents the parent of each element in the set.
	ranks []int // ranks array stores the rank of each element.
}

// find method implements the find operation for the disjoint-set data structure.
// It returns the representative (root) of the set that element x belongs to.
// Path compression technique is used here to optimize subsequent find operations.
func (ds *disjointSet) find(x int) int {
	if ds.roots[x] == x {
		return x
	}
	ds.roots[x] = ds.find(ds.roots[x])
	return ds.roots[x]
}

// union method implements the union (or merge) operation for the disjoint-set data structure.
// It replaces the set containing element x and the set containing element y with their union.
// Union by rank is used here to optimize the union operation.
func (ds *disjointSet) union(x, y int) {
	rootX := ds.find(x)
	rootY := ds.find(y)
	if rootX == rootY {
		return
	}
	rankX := ds.ranks[rootX]
	rankY := ds.ranks[rootY]
	if rankX > rankY {
		ds.roots[rootY] = rootX
		return
	}
	if rankX < rankY {
		ds.roots[rootX] = rootY
		return
	}
	ds.roots[rootX] = rootY
	ds.ranks[rootY] += 1
}

// isConnected method checks if two elements x and y are in the same set.
// It returns true if x and y are in the same set, otherwise false.
func (ds *disjointSet) isConnected(x, y int) bool {
	return ds.find(x) == ds.find(y)
}

// newDisjointSet function creates a new disjoint-set data structure with n elements.
// Initially, each element is in a separate set.
func newDisjointSet(n int) *disjointSet {
	roots := make([]int, n)
	ranks := make([]int, n)
	for i := range n {
		roots[i] = i
		ranks[i] = 1
	}
	newDisjointSet := disjointSet{roots, ranks}
	return &newDisjointSet
}

// validPath function checks if there is a valid path between source and destination in the given graph.
// The graph is represented by n nodes and a list of edges.
// It uses the disjoint-set data structure to check the connectivity between source and destination.
// It returns true if there is a valid path, otherwise false.
func validPath(n int, edges [][]int, source int, destination int) bool {
	ds := newDisjointSet(n)
	for _, edge := range edges {
		ds.union(edge[0], edge[1])
	}
	return ds.isConnected(source, destination)
}
