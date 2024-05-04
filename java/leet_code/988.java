import java.util.Arrays;

/**
 * This class represents a node in a binary tree.
 * Each node has a value, a left child, and a right child.
 *
 * @author jerodg
 */
public class TreeNode {
    private int val = 0;
    private TreeNode left = null;
    private TreeNode right = null;

    /**
     * Default constructor.
     */
    TreeNode() {
        super();
    }

    /**
     * Constructor with value.
     *
     * @param val The value of the node. It is a non-negative integer.
     */
    TreeNode(final int val) {
        super();
        this.setVal(val);
    }

    /**
     * Constructor with value, left child, and right child.
     *
     * @param val   The value of the node. It is a non-negative integer.
     * @param left  The left child of the node. It is an instance of TreeNode.
     * @param right The right child of the node. It is an instance of TreeNode.
     */
    TreeNode(final int val, final TreeNode left, final TreeNode right) {
        super();
        this.setVal(val);
        this.setLeft(left);
        this.setRight(right);
    }

    /**
     * Getter for the value of the node.
     *
     * @return The value of the node. It is a non-negative integer.
     */
    int getVal() {
        return val;
    }

    /**
     * Setter for the value of the node.
     *
     * @param val The value to be set. It is a non-negative integer.
     */
    private void setVal(int val) {
        this.val = val;
    }

    /**
     * Getter for the left child of the node.
     *
     * @return The left child of the node. It is an instance of TreeNode.
     */
    public TreeNode getLeft() {
        return left;
    }

    /**
     * Setter for the left child of the node.
     *
     * @param left The left child to be set. It is an instance of TreeNode.
     */
    public void setLeft(TreeNode left) {
        this.left = left;
    }

    /**
     * Getter for the right child of the node.
     *
     * @return The right child of the node. It is an instance of TreeNode.
     */
    public TreeNode getRight() {
        return right;
    }

    /**
     * Setter for the right child of the node.
     *
     * @param right The right child to be set. It is an instance of TreeNode.
     */
    public void setRight(TreeNode right) {
        this.right = right;
    }
}

/**
 * This class provides a solution for the problem of finding the smallest string starting from the leaf of a binary tree.
 * The problem is solved by using a depth-first search to find the smallest string starting from each leaf of the tree.
 * The smallest string is updated at each leaf.
 *
 * @author jerodg
 */
class Solution {

    // Array to store the characters of the smallest string
    private char[] chs = null;
    // Index to keep track of the start of the smallest string in the array
    private int l = 0;

    /**
     * This method calculates the depth of the binary tree.
     *
     * @param root The root node of the binary tree. It is an instance of TreeNode.
     *
     * @return The depth of the binary tree. It is a non-negative integer.
     */
    private static int depth(final TreeNode root) {
        if (root == null) {
            return 0;
        }
        // The depth of the tree is the maximum depth of its left and right subtrees plus one
        return Math.max(Solution.depth(root.getLeft()), Solution.depth(root.getRight())) + 1;
    }

    /**
     * This method returns the smallest string starting from the leaf of the binary tree.
     *
     * @param root The root node of the binary tree. It is an instance of TreeNode.
     *
     * @return The smallest string starting from the leaf. It is a string of characters.
     */
    public String smallestFromLeaf(final TreeNode root) {
        // Calculate the depth of the tree
        final int d = Solution.depth(root);
        // Start the recursive function to find the smallest string
        this.solve(root, new char[d], d - 1);
        // Return the smallest string
        return new String(this.getChs(), this.l, d - this.l);
    }

    /**
     * This method recursively finds the smallest string starting from the leaf of the binary tree.
     *
     * @param node The current node. It is an instance of TreeNode.
     * @param t    The array to store the characters of the current string. It is an array of characters.
     * @param i    The index to insert the character of the current node into the array. It is a non-negative integer.
     */
    private void solve(final TreeNode node, final char[] t, final int i) {
        if (node == null) {
            return;
        }
        // Convert the value of the node to a character and insert it into the array
        t[i] = (char) ((int) 'a' + node.getVal());
        // If the node is a leaf node
        if (node.getLeft() == null && node.getRight() == null) {
            // If this is the first leaf node
            if (this.getChs() == null) {
                this.chs = Arrays.copyOf(t, t.length);
                this.l = i;
            } else {
                // Compare the current string with the smallest string
                for (int k = 0, d = Math.max(this.l, i); k + d < t.length; k++) {
                    if (this.getChs()[this.l + k] < t[i + k]) {
                        return;
                    } else if (this.getChs()[this.l + k] > t[i + k]) {
                        this.chs = Arrays.copyOf(t, t.length);
                        this.l = i;
                        return;
                    }
                }
                if (this.l < i) {
                    this.chs = Arrays.copyOf(t, t.length);
                    this.l = i;
                }
            }
            return;
        }
        // Continue the recursion on the left and right subtrees
        this.solve(node.getLeft(), t, i - 1);
        this.solve(node.getRight(), t, i - 1);
    }

    /**
     * Getter for the array of characters of the smallest string.
     *
     * @return The array of characters of the smallest string. It is an array of characters.
     */
    private char[] getChs() {
        return this.chs;
    }

    /**
     * Setter for the array of characters of the smallest string.
     *
     * @param chs The array of characters to be set. It is an array of characters.
     */
    public void setChs(final char[] chs) {
        this.chs = chs.clone();
    }

    /**
     * Getter for the start of the smallest string in the array.
     *
     * @return The start of the smallest string in the array. It is a non-negative integer.
     */
    public int getL() {
        return this.l;
    }

    /**
     * Setter for the start of the smallest string in the array.
     *
     * @param l The start to be set. It is a non-negative integer.
     */
    public void setL(final int l) {
        this.l = l;
    }
}
