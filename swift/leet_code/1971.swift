class Solution {
    func validPath(_ n: Int, _ edges: [[Int]], _ source: Int, _ destination: Int) -> Bool {
        struct UnionFind {
            var nodes: [Int]
            init(_ count: Int) {
                nodes = Array(0 ..< count)
            }

            mutating func find(_ node: Int) -> Int {
                if nodes[node] == node {
                    return node
                }
                nodes[node] = find(nodes[node])
                return nodes[node]
            }

            mutating func union(_ x: Int, _ y: Int) {
                let xRoot = find(x)
                let yRoot = find(y)
                if xRoot != yRoot {
                    nodes[xRoot] = yRoot
                }
            }
        }
        var disjointSet = UnionFind(n)
        for edge in edges {
            disjointSet.union(edge[0], edge[1])
        }
        return disjointSet.find(source) == disjointSet.find(destination)
    }
}
