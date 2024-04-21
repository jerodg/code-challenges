import Foundation

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */

struct Solution {
    /**
     * This function returns the smallest string that starts from a leaf of a binary tree and ends at its root.
     * The binary tree is mapped to a string by adding the ASCII value of 'a' to the node value and converting it to a character.
     * The function is optimized for speed.
     *
     * @param root: The root of the binary tree.
     * @param suffix: The suffix string to append to the current node's character. Default is an empty string.
     * @return: The smallest string that starts from a leaf and ends at the root.
     */
    @_optimize(speed)
    func smallestFromLeaf(_ root: TreeNode?, _ suffix: String = "") -> String {
        // If the root is nil, return an empty string
        guard let root else { return "" }

        // Convert the node value to a character and append the suffix
        let current = String(UnicodeScalar(UInt8(97 + root.val))) + suffix

        // If the node is a leaf, return the current string
        if root.left == nil, root.right == nil {
            return current
        }

        // Recursively call the function for the left and right children
        let left = root.left.map { smallestFromLeaf($0, current) }
        let right = root.right.map { smallestFromLeaf($0, current) }

        // Return the smallest string between the left and right children
        // If one of them is nil, return the other
        if let left, let right {
            return left < right ? left : right
        } else if left == nil {
            return right ?? ""
        } else {
            return left ?? ""
        }
    }
}
