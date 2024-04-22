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
    public $val = null;
    public $left = null;
    public $right = null;

    /**
     * TreeNode constructor.
     *
     * @param int|null $val The value of the node.
     * @param TreeNode|null $left The left child of the node.
     * @param TreeNode|null $right The right child of the node.
     */
    public function __construct($val = 0, $left = null, $right = null)
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
    /**
     * Adds a row of nodes with a given value at a given depth in a binary tree.
     *
     * This method takes a binary tree, a value, and a depth, and adds a row of nodes with the given value at the given depth in the tree.
     *
     * @param TreeNode|null $root The root of the binary tree.
     * @param int $val The value of the nodes in the new row.
     * @param int $depth The depth at which to add the new row.
     *
     * @return TreeNode|null The root of the binary tree after adding the new row.
     *
     * @throws InvalidArgumentException If $depth is less than 1.
     *
     * @example
     * $solution = new Solution();
     * $root = new TreeNode(4, new TreeNode(2, new TreeNode(3), new TreeNode(1)), new TreeNode(6, new TreeNode(5)));
     * $newRoot = $solution->addOneRow($root, 1, 2);
     * // The binary tree now looks like this:
     * //     4
     * //   /   \
     * //  1     1
     * // /       \
     * //2         6
     * // / \     /
     * //3   1   5
     */
    public function addOneRow(?TreeNode $root, int $val, int $depth): ?TreeNode
    {
        if ($depth === 1) {
            return new TreeNode($val, $root, null);
        }
        if (!$root) {
            return [];
        }

        $res = $root;
        $sample = new TreeNode($val);
        $arr = [$root];
        $counter = 2;
        while (count($arr) > 0) {
            $tmp = [];
            foreach ($arr as $v) {
                if ($counter === $depth) {
                    $left = clone $sample;
                    $right = clone $sample;
                    if ($v->left) {
                        $left->left = $v->left;
                    }
                    if ($v->right) {
                        $right->right = $v->right;
                    }
                    $v->left = $left;
                    $v->right = $right;
                }
                if ($v->left) {
                    $tmp[] = $v->left;
                }
                if ($v->right) {
                    $tmp[] = $v->right;
                }
            }
            $arr = $tmp;
            if ($counter === $depth) {
                break;
            }

            $counter++;
        }
        return $res;
    }
}
