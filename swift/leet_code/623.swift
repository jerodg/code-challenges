// MARK: - TreeNode
/**
 A class that represents a node in a binary tree.
 Each node has a value and two children: left and right.
 */
public class TreeNode {
    public var val: Int
    public var left: TreeNode?
    public var right: TreeNode?

    /// Default initializer
    public init() { val = 0; left = nil; right = nil }

    /// Initializer with value
    /// - Parameter val: The value of the node
    public init(_ val: Int) { self.val = val; left = nil; right = nil }

    /// Initializer with value and children
    /// - Parameters:
    ///   - val: The value of the node
    ///   - left: The left child of the node
    ///   - right: The right child of the node
    public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

// MARK: - Solution
/**
 A class that provides a solution to the problem of adding a row to a binary tree.
 */
class Solution {
    /**
     Adds a row to a binary tree.

     This function adds a row of nodes with a given value at a given depth in the tree.
     The original nodes at this depth will become the children of the new nodes.

     - Parameters:
       - root: The root of the binary tree.
       - val: The value of the new nodes.
       - depth: The depth at which to add the new row.

     - Returns: The root of the modified tree.

     - Precondition: `depth` > 0

     - Postcondition: The tree has a new row of nodes at the specified depth.

     - Throws: This function throws a fatal error if it cannot add a row at the specified depth.

     - Example:
       ```
       let root = TreeNode(1)
       root.left = TreeNode(2)
       root.right = TreeNode(3)
       let solution = Solution()
       let newRoot = solution.addOneRow(root, 4, 2)
       // The tree now looks like this:
       //     1
       //    / \
       //   4   4
       //  /     \
       // 2       3
       ```
     */
    func addOneRow(_ root: TreeNode?, _ val: Int, _ depth: Int) -> TreeNode? {
        guard depth > 1 else {
            let r = TreeNode(val, root, nil); return r
        }
        var queue = [root!], dp = 2
        while true {
            guard dp == depth else {
                queue = queue.flatMap { [$0.left, $0.right] }.compactMap { $0 }
                dp += 1
                continue
            }
            for item in queue {
                item.left = TreeNode(val, item.left, nil)
                item.right = TreeNode(val, nil, item.right)
            }
            return root
        }
        fatalError()
    }
}
