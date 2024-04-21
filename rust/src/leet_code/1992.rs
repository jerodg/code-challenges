use std::vec::Vec;

/// This module contains the implementation of the `Solution` struct.
///
/// The `Solution` struct provides a method `find_farmland` which finds the farmland in a given land matrix.
/// The function takes a 2D vector of integers representing the land matrix, where 1 represents farmland and 0 represents non-farmland.
/// It returns a 2D vector of integers where each inner vector represents a rectangle of farmland. The rectangle is represented by the coordinates of its top-left and bottom-right corners.
///
/// # Errors
///
/// This function will panic if the land matrix is empty.
impl Solution {
    /// Finds the farmland in a given land matrix.
    ///
    /// # Parameters
    ///
    /// * `land` - A 2D vector of integers representing the land matrix.
    ///
    /// # Returns
    ///
    /// * `Vec<Vec<i32>>` - A 2D vector of integers where each inner vector represents a rectangle of farmland.
    pub fn find_farmland(land: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        // Initialize the result vector and the visited matrix
        let mut res = vec![];
        let n = land.len();
        let m = land[0].len();
        let mut visited = vec![vec![false; m]; n];

        // Iterate over the land matrix
        for i in 0..n {
            for j in 0..m {
                // If the current cell is farmland and has not been visited yet
                if land[i][j] == 1 && !visited[i][j] {
                    let mut x = i;
                    let mut y = j;

                    // Find the bottom-right corner of the farmland rectangle
                    while x < n && land[x][j] == 1 {
                        x += 1;
                    }
                    while y < m && land[i][y] == 1 {
                        y += 1;
                    }

                    // Add the rectangle to the result
                    res.push(vec![i as i32, j as i32, x as i32 - 1, y as i32 - 1]);

                    // Mark all the cells in the rectangle as visited
                    for p in i..x {
                        for q in j..y {
                            visited[p][q] = true;
                        }
                    }
                }
            }
        }

        // Return the result
        res
    }
}