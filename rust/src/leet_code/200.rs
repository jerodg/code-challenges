//! This module provides a solution for the problem of counting the number of islands in a 2D grid.
//! Each cell in the grid can be '1' (land) or '0' (water). An island is surrounded by water and is
//! formed by connecting adjacent lands horizontally or vertically. This module provides a function
//! `num_islands` that counts the number of islands.

/// Struct `Solution` is a placeholder for the solution methods.
impl Solution {
    /// Counts the number of islands in a 2D grid map.
    ///
    /// # Parameters
    ///
    /// * `grid` - A 2D vector of characters. Each character can be '1' (land) or '0' (water).
    ///
    /// # Returns
    ///
    /// * An `i32` integer representing the number of islands in the grid.
    ///
    /// # Example
    ///
    /// ```
    /// let grid = vec![
    ///     vec!['1', '1', '1', '1', '0'],
    ///     vec!['1', '1', '0', '1', '0'],
    ///     vec!['1', '1', '0', '0', '0'],
    ///     vec!['0', '0', '0', '0', '0'],
    /// ];
    /// assert_eq!(Solution::num_islands(grid), 1);
    /// ```
    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {
        let (len_outer, len_inner) = (grid.len(), grid[0].len());
        let mut _grid = grid
            .iter()
            .enumerate()
            .flat_map(|(id, e)| e.iter().enumerate().map(move |(id2, val)| ((id, id2), val)))
            .filter(|(_, val)| *val == &'1');
        let mut output = 0;
        let mut cache = Vec::<(usize, usize)>::with_capacity(len_inner * len_outer);
        let mut _cache = vec![false; len_inner * len_outer];
        while let Some(((i, j), _)) = _grid.next() {
            if !_cache[i * len_inner + j] {
                output += 1;
                cache.push((i, j));
            }
            while let Some((i, j)) = cache.pop() {
                _cache[i * len_inner + j] = true;
                if i + 1 < len_outer && !_cache[(i + 1) * len_inner + j] && grid[i + 1][j] == '1' {
                    cache.push((i + 1, j));
                }
                if i > 0 && !_cache[(i - 1) * len_inner + j] && grid[i - 1][j] == '1' {
                    cache.push((i - 1, j));
                }
                if j + 1 < len_inner && !_cache[i * len_inner + j + 1] && grid[i][j + 1] == '1' {
                    cache.push((i, j + 1));
                }
                if j > 0 && !_cache[i * len_inner + j - 1] && grid[i][j - 1] == '1' {
                    cache.push((i, j - 1));
                }
            }
        }
        output
    }
}