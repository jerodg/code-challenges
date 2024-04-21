<?php

/**
 * This file contains the TreeNode and Solution classes.
 *
 * PHP version 8.3
 *
 * @category LeetCode
 * @package  LeetCode\Solution
 * @author   Jerodg
 * @license  http://opensource.org/licenses/gpl-license.php GNU Public License
 * @link     http://github.com/jerodg/leet_code
 */

declare(strict_types=1);

/**
 * The TreeNode class represents a node in a binary tree.
 *
 * @category LeetCode
 * @package  LeetCode\Solution
 * @author   Jerodg
 * @license  http://opensource.org/licenses/gpl-license.php GNU Public License
 * @link     http://github.com/jerodg/leet_code
 */
class TreeNode
{
    public mixed $val = null;
    public ?TreeNode $left = null;
    public ?TreeNode $right = null;

    /**
     * TreeNode constructor.
     *
     * @param mixed $val The value of the node.
     * @param TreeNode|null $left The left child of the node.
     * @param TreeNode|null $right The right child of the node.
     */
    public function __construct(mixed $val = 0, ?TreeNode $left = null, ?TreeNode $right = null)
    {
        $this->val = $val;
        $this->left = $left;
        $this->right = $right;
    }
}

/**
 * The Solution class contains methods for solving specific problems related to binary trees.
 *
 * @category LeetCode
 * @package  LeetCode\Solution
 * @author   Jerodg
 * @license  http://opensource.org/licenses/gpl-license.php GNU Public License
 * @link     http://github.com/jerodg/leet_code
 */
class Solution
{
    private ?string $res;

    /**
     * Returns the smallest string that starts from leaf and one end of this string is a leaf of the tree.
     *
     * @param TreeNode|null $root The root of the tree.
     *
     * @return string|null The smallest string that starts from leaf.
     *
     * @throws InvalidArgumentException If $root is not an instance of TreeNode.
     *
     * @example
     * $solution = new Solution();
     * $smallestFromLeaf = $solution->smallestFromLeaf(new TreeNode(0, new TreeNode(1), new TreeNode(2)));
     * echo $smallestFromLeaf; // Outputs: "ba"
     */
    public function smallestFromLeaf(?TreeNode $root): ?string
    {
        $this->res = null;
        $this->smallest($root, '');
        return $this->res;
    }

    /**
     * Helper function to find the smallest string that starts from leaf.
     *
     * @param TreeNode|null $root The root of the tree.
     * @param string $s The current string.
     *
     * @return void
     *
     * @throws InvalidArgumentException If $root is not an instance of TreeNode or $s is not a string.
     *
     * @example
     * $solution = new Solution();
     * $solution->smallest(new TreeNode(0, new TreeNode(1), new TreeNode(2)), "");
     */
    private function smallest(?TreeNode $root, string $s): void
    {
        if (!$root) {
            return;
        }

        $s = chr(97 + $root->val) . $s;
        $this->smallest($root->left, $s);
        $this->smallest($root->right, $s);

        if (!$root->left && !$root->right &&
            (!$this->res || $this->res > $s)) {
            $this->res = $s;
        }
    }
}
