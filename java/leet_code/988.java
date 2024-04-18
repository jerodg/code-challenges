import javax.swing.tree.TreeNode;
import java.util.Arrays;

/*
  Definition for a binary tree node.
  public class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;
  TreeNode() {}
  TreeNode(int val) { this.val = val; }
  TreeNode(int val, TreeNode left, TreeNode right) {
  this.val = val;
  this.left = left;
  this.right = right;
  }
  }
 */

/**
 * This class provides a solution for finding the smallest string starting from the leaf of a binary tree.
 * The binary tree nodes contain values from 0 to 25 mapped to lowercase English letters 'a' to 'z'.
 */
class Solution {

    // Array to store the characters of the smallest string
    private char[] chs = null;
    // Index to keep track of the start of the smallest string in the array
    private int l = 0;

    /**
     * This method returns the smallest string starting from the leaf of the binary tree.
     * @param root The root node of the binary tree.
     * @return The smallest string starting from the leaf.
     */
    public String smallestFromLeaf(final TreeNode root) {
        // Calculate the depth of the tree
        final int d = this.depth(root);
        // Start the recursive function to find the smallest string
        this.solve(root, new char[d], d - 1);
        // Return the smallest string
        return new String(this.getChs(), getL(), d - getL());
    }

    /**
     * This method calculates the depth of the binary tree.
     * @param root The root node of the binary tree.
     * @return The depth of the binary tree.
     */
    private int depth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        // The depth of the tree is the maximum depth of its left and right subtrees plus one
        return Math.max(depth(root.left), depth(root.right)) + 1;
    }

    /**
     * This method recursively finds the smallest string starting from the leaf of the binary tree.
     * @param node The current node.
     * @param t The array to store the characters of the current string.
     * @param i The index to insert the character of the current node into the array.
     */
    private void solve(TreeNode node, char[] t, int i) {
        if (node == null) {
            return;
        }
        // Convert the value of the node to a character and insert it into the array
        t[i] = (char) ('a' + node.val);
        // If the node is a leaf node
        if (node.left == null && node.right == null) {
            // If this is the first leaf node
            if (getChs() == null) {
                setChs(Arrays.copyOf(t, t.length));
                setL(i);
            } else {
                // Compare the current string with the smallest string
                for (int k = 0, d = Math.max(getL(), i); k + d < t.length; k++) {
                    if (getChs()[getL() + k] < t[i + k]) {
                        return;
                    } else if (getChs()[getL() + k] > t[i + k]) {
                        setChs(Arrays.copyOf(t, t.length));
                        setL(i);
                        return;
                    }
                }
                if (getL() < i) {
                    setChs(Arrays.copyOf(t, t.length));
                    setL(i);
                }
            }
            return;
        }
        // Continue the recursion on the left and right subtrees
        solve(node.left, t, i - 1);
        solve(node.right, t, i - 1);
    }

    public char[] getChs() {
        return chs;
    }

    public void setChs(char[] chs) {
        this.chs = chs;
    }

    public int getL() {
        return l;
    }

    public void setL(int l) {
        this.l = l;
    }
}
