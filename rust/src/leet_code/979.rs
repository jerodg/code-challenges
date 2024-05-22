#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    fn dfs(node: &Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
        node.as_ref().map_or((0, 0), |node| {
            let bn = node.borrow();
            let (leftcount, leftdiff) = Self::dfs(&bn.left);
            let (rightcount, rightdiff) = Self::dfs(&bn.right);
            let diff = leftdiff + rightdiff + bn.val - 1;
            let count = leftcount + rightcount + diff.abs();
            (count, diff)
        })
    }

    pub fn distribute_coins(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Self::dfs(&root).0
    }
}
