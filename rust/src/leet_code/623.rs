// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }

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
use std::cell::RefCell;
use std::rc::Rc;

// Defining a type alias for `Option<Rc<RefCell<TreeNode>>>` for convenience
type OptNode = Option<Rc<RefCell<TreeNode>>>;

/// This module contains the implementation of the `Solution` struct.
///
/// The `Solution` struct provides a method `add_one_row` which adds a row of nodes with a given value to a binary tree at a given depth.
/// The function takes an optional reference-counted, mutable reference to the root node of the tree, an integer value for the new nodes, and an integer depth.
/// It returns an optional reference-counted, mutable reference to the root node of the modified tree.
///
/// # Parameters
///
/// * `root` - An optional reference-counted, mutable reference to the root node of the tree.
/// * `val` - An integer value for the new nodes.
/// * `depth` - An integer depth at which to add the new row of nodes.
///
/// # Returns
///
/// * `OptNode` - An optional reference-counted, mutable reference to the root node of the modified tree.
///
/// # Errors
///
/// This function will return `None` if the root node is `None`.
impl Solution {
    pub fn add_one_row(root: OptNode, val: i32, depth: i32) -> OptNode {
        // If the root node is None, return None
        if root.is_none() {
            return None;
        }

        // Define a closure to create a new node with a given value and optional left and right child nodes
        let new_node = |left: OptNode, right: OptNode, val: i32| -> OptNode {
            Some(Rc::new(RefCell::new(TreeNode { val, left, right })))
        };

        // If the root node is Some, borrow it mutably
        if let Some(ref rc_node) = root {
            let mut node = rc_node.borrow_mut();
            // Match on the depth
            match depth {
                // If the depth is 1, return a new node with the root node as its left child and None as its right child
                1 => {
                    return new_node(root.clone(), None, val);
                }
                // If the depth is 2, replace the left and right child nodes of the root node with new nodes
                2 => {
                    node.left = new_node(node.left.take(), None, val);
                    node.right = new_node(None, node.right.take(), val);
                }
                // If the depth is greater than 2, recursively call `add_one_row` on the left and right child nodes of the root node
                _ => {
                    Self::add_one_row(node.left.clone(), val, depth - 1);
                    Self::add_one_row(node.right.clone(), val, depth - 1);
                }
            }
        }
        // Return the root node
        root
    }
}