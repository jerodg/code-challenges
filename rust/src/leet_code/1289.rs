//! # LeetCode Problem 1289
//!
//! This module contains the solution for LeetCode problem 1289. The problem is about finding the
//! minimum falling path sum in a grid. The function `min_falling_path_sum` takes a 2D vector as
//! input and returns the minimum falling path sum. The function uses dynamic programming to solve
//! the problem. The time complexity for the provided Rust code is O(n^2), where n is the length of
//! the grid. The space complexity of the function is O(n), where n is the length of the grid.
//!
//! The selected Rust code is a solution for the LeetCode problem 1289, which is about finding
//! the minimum falling path sum in a grid. The function `min_falling_path_sum` uses dynamic
//! programming to solve the problem.
//!
//! Here is the time complexity analysis for the selected code:
//!
//! - Best Case: O(n^2), where n is the length of the grid. This is because even in the best
//! case, the function needs to iterate over each row and each column in the grid at least once.
//!
//! - Average Case: O(n^2), where n is the length of the grid. The function iterates over each
//! row and each column in the grid exactly once. The operations inside the nested loop
//! (finding the smallest and second smallest elements in the previous row, calculating the minimum
//! falling path sum for the current row) all take constant time.
//!
//! - Worst Case: O(n^2), where n is the length of the grid. Even in the worst case, the function
//! still needs to iterate over each row and each column in the grid once. The operations inside the
//! nested loop do not change based on the input, so they always take constant time.
//!
//! The space complexity of the function is O(n), where n is the length of the grid. This is
//! because the size of the `prev_row` and `curr_row` vectors is equal to the length of the grid,
//! which does not depend on the size of the input grid, so the space complexity is linear.

impl Solution {
    /// Finds the minimum falling path sum in a grid.
    ///
    /// # Parameters
    ///
    /// * `grid` - A 2D vector of 32-bit integers.
    ///
    /// # Returns
    ///
    /// * A 32-bit integer representing the minimum falling path sum.
    ///
    /// # Errors
    ///
    /// This function will panic if the grid is empty.
    pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        // The length of the grid
        let n = grid.len();

        // If the grid only contains one row, return the first element
        if n == 1 {
            return grid[0][0];
        }

        // The previous row in the grid
        let mut prev_row: Vec<i32> = grid[0].clone();

        // Iterate over the rows in the grid
        for i in 1..n {
            // The current row in the grid
            let mut curr_row: Vec<i32> = vec![0; n];
            // The smallest and second smallest elements in the previous row
            let mut min1: i32 = i32::MAX;
            let mut min2: i32 = i32::MAX;

            // The indices of the smallest and second smallest elements in the previous row
            let mut idx1: i32 = -1;
            let mut idx2: i32 = -1;

            // Find the smallest and second smallest elements in the previous row
            for j in 0..n {
                if prev_row[j] < min1 {
                    min2 = min1;
                    min1 = prev_row[j];
                    idx2 = idx1;
                    idx1 = j as i32;
                } else if prev_row[j] < min2 {
                    min2 = prev_row[j];
                    idx2 = j as i32;
                }
            }

            // Calculate the minimum falling path sum for the current row
            for j in 0..n {
                if j as i32 == idx1 {
                    curr_row[j] = grid[i][j] + min2;
                } else {
                    curr_row[j] = grid[i][j] + min1;
                }
            }

            // Update the previous row to be the current row
            prev_row = curr_row;
        }

        // Return the minimum element in the last row
        *prev_row.iter().min().unwrap()
    }
}
