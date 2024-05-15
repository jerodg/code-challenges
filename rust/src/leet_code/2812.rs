// Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
//
// This program is free software: you can redistribute it and/or modify it under the terms of the
// Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
// or (at your option) any later version.
//
// This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
// even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
// for more details.
//
// The above copyright notice and this permission notice shall be included in all copies or
// substantial portions of the Software. You should have received a copy of the SSPL along with this
// program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.

// Package leet_code
//
// This file contains the implementation of the Solution struct and its associated methods.
// The main purpose of this file is to solve the problem described in LeetCode 2812.
// The solution involves calculating the maximum safeness factor of a grid.

use std::collections::{BinaryHeap, VecDeque};

impl Solution {
    // NEIGHBORS is a constant that represents the possible directions in which we can move in the grid.
    const NEIGHBORS: [(i32, i32); 4] = [(1, 0), (0, 1), (-1, 0), (0, -1)];

    /// The `maximum_safeness_factor` method calculates the maximum safeness factor of a grid.
    ///
    /// # Parameters
    ///
    /// * `grid` - A mutable reference to a 2D vector of integers representing the grid.
    ///
    /// # Returns
    ///
    /// * An integer representing the maximum safeness factor of the grid.
    ///
    /// # Errors
    ///
    /// This function will panic if the grid is empty.
    pub fn maximum_safeness_factor(mut grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        // The `valid_neighbors` closure returns a list of valid neighbors for a given cell in the grid.
        let valid_neighbors = |(i, j): (usize, usize)| {
            let (n, r, c) = (n as i32, i as i32, j as i32);
            Self::NEIGHBORS
                .iter()
                .map(move |(dr, dc)| (r + dr, c + dc))
                .filter(move |&(x, y)| 0 <= x && x < n && 0 <= y && y < n)
                .map(|(x, y)| (x as usize, y as usize))
        };

        // Initialize the queue with the cells that are not obstacles.
        let mut queue: VecDeque<_> = (0..n)
            .flat_map(|i| (0..n).map(move |j| (i, j)))
            .filter_map(|(i, j)| match grid[i][j] {
                0 => {
                    grid[i][j] = -1;
                    None
                }
                _ => {
                    grid[i][j] = 0;
                    Some((i, j))
                }
            })
            .collect();
        let mut alt = queue.clone();

        // Calculate the safeness factor for each cell in the grid.
        while !queue.is_empty() {
            alt.clear();
            while let Some((r, c)) = queue.pop_front() {
                alt.extend(valid_neighbors((r, c)).filter_map(|(x, y)| {
                    if grid[x][y] != -1 {
                        return None;
                    }
                    grid[x][y] = grid[r][c] + 1;
                    Some((x, y))
                }));
            }
            std::mem::swap(&mut queue, &mut alt)
        }

        // Use a binary heap to find the cell with the maximum safeness factor.
        let mut heap = BinaryHeap::from([(grid[0][0], 0, 0)]);
        while let Some((safety, i, j)) = heap.pop() {
            if i == n - 1 && j == n - 1 {
                return safety;
            }
            heap.extend(valid_neighbors((i, j)).filter_map(|(x, y)| {
                let val = grid[x][y];
                if val == -1 {
                    return None;
                }
                grid[x][y] = -1;
                Some((safety.min(val), x, y))
            }));
        }
        -1
    }
}
