use std::cmp::max;

/// This module provides a solution for the problem of finding the maximal rectangle in a matrix.
/// The matrix is represented as a vector of vectors of characters, where '1' represents a filled cell and '0' represents an empty cell.
/// The function `maximal_rectangle` finds the largest rectangle consisting of '1's in the given matrix and returns its area.

impl Solution {
    /// Finds the maximal rectangle in a matrix.
    ///
    /// # Arguments
    ///
    /// * `matrix` - A vector of vectors of characters representing the matrix.
    ///
    /// # Returns
    ///
    /// * An i32 representing the area of the maximal rectangle.
    pub fn maximal_rectangle(matrix: Vec<Vec<char>>) -> i32 {
        // Initialize the height vector with zeros
        let mut h: Vec<i32> = vec![0; matrix[0].len()];
        // Initialize the result
        let mut res = 0;
        // Iterate over the rows of the matrix
        for i in 0..matrix.len() {
            // Initialize the stack
            let mut v: Vec<usize> = vec![];
            // Iterate over the columns of the matrix
            for j in 0..matrix[i].len() {
                // Update the height vector
                h[j] = if matrix[i][j] == '0' { 0 } else { h[j] + 1 };
                // Process the stack
                loop {
                    match v.last_mut() {
                        // If the current height is less than the height at the top of the stack
                        Some(&mut k) if h[k] > h[j] => {
                            v.pop();
                            res = max(
                                res,
                                h[k] * (j as i32 - if v.is_empty() { -1 } else { *v.last().unwrap() as i32 } - 1),
                            );
                        }
                        // If the current height is equal to the height at the top of the stack
                        Some(p) if h[*p] == h[j] => {
                            *p = j;
                            break;
                        }
                        // If the stack is empty or the current height is greater than the height at the top of the stack
                        _ => {
                            v.push(j);
                            break;
                        }
                    }
                }
            }
            // Process the remaining elements in the stack
            while let Some(k) = v.pop() {
                res = max(
                    res,
                    h[k] * (matrix[i].len() as i32 - if v.is_empty() { -1 } else { *v.last().unwrap() as i32 } - 1),
                );
            }
        }
        // Return the result
        res
    }
}
