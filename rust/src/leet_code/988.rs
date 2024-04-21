// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;

use std::rc::Rc;
use std::cell::RefCell;

/// This module contains the implementation of the `Solution` struct.
///
/// The `Solution` struct provides two methods: `dfs` and `smallest_from_leaf`.
/// The `dfs` method is a helper function used to perform a depth-first search on a binary tree.
/// The `smallest_from_leaf` method returns the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
///
/// # Structs
///
/// * `Solution` - The main struct in this module.
///
/// # Methods
///
/// * `dfs` - Performs a depth-first search on a binary tree.
/// * `smallest_from_leaf` - Returns the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
impl Solution {
    /// Performs a depth-first search on a binary tree.
    ///
    /// # Parameters
    ///
    /// * `node` - A reference to an optional `Rc<RefCell<TreeNode>>`.
    /// * `res` - A mutable reference to a `String`.
    /// * `path` - A mutable `String`.
    ///
    /// # Returns
    ///
    /// This method does not return a value.
    pub fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, res: &mut String, mut path: String) {
        // If the node is Some, borrow it
        if let Some(node) = node {
            let node = node.borrow();
            // Push the node value to the path
            path.push((node.val as u8 + b'a') as char);
            // If the node is a leaf node
            if node.left.is_none() && node.right.is_none() {
                // Reverse the path and collect it into a String
                let path = path.chars().rev().collect::<String>();
                // If res is empty or path is lexicographically smaller than res, assign path to res
                if res.is_empty() || path < *res {
                    *res = path;
                }
            }
            // Recursively call dfs on the left and right child nodes
            Self::dfs(&node.left, res, path.clone());
            Self::dfs(&node.right, res, path);
        }
    }

    /// Returns the lexicographically smallest string that starts at a leaf of this tree and ends at the root.
    ///
    /// # Parameters
    ///
    /// * `root` - An optional `Rc<RefCell<TreeNode>>`.
    ///
    /// # Returns
    ///
    /// * `String` - The lexicographically smallest string that starts at a leaf of this tree and ends at the root.
    pub fn smallest_from_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> String {
        // Initialize res as an empty String
        let mut res = String::new();
        // Call dfs on the root node
        Self::dfs(&root, &mut res, String::new());
        // Return res
        res
    }
}