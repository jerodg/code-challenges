// Copyright © 2010-2024 https://github.com/jerodg/
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
// program. If not, see https://www.mongodb.com/licensing/server-side-public-license.

// Package leet_code
//
// This file contains the implementation of the Solution struct and its associated methods.
// The main purpose of this file is to solve the problem from LeetCode: https://leetcode.com/problems/path-with-maximum-gold/
// The problem is about finding the maximum amount of gold that can be collected by starting from any cell in the given grid.

use std::collections::HashMap;

// Graph is a type alias for a vector of tuples. Each tuple contains an integer and a vector of usize.
// The integer represents the amount of gold in a cell, and the vector represents the indices of the neighboring cells.
type Graph = Vec<(i32, Vec<usize>)>;

impl Solution {
    /// Constructs a graph from the given grid.
    ///
    /// The graph is represented as a vector of tuples. Each tuple contains an integer and a vector of usize.
    /// The integer represents the amount of gold in a cell, and the vector represents the indices of the neighboring cells.
    ///
    /// # Arguments
    ///
    /// * `grid` - A vector of vectors of i32. Each inner vector represents a row in the grid.
    ///
    /// # Returns
    ///
    /// * A Graph, which is a vector of tuples. Each tuple contains an integer and a vector of usize.
    fn construct_graph(grid: Vec<Vec<i32>>) -> Graph {
        let mut hm = HashMap::new();
        let mut result = Graph::new();
        let (m, n) = (grid.len(), grid[0].len());
        for r in 0..m {
            for c in 0..n {
                if grid[r][c] != 0 {
                    hm.insert((r, c), result.len());
                    result.push((grid[r][c], Vec::new()))
                }
            }
        }
        for ((r, c), i) in hm.iter() {
            let (r, c) = (*r as isize, *c as isize);
            for (rd, cd) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                let (rn, cn) = (r + rd, c + cd);
                if rn < 0 || cn < 0 { continue; }
                let (rn, cn) = (rn as usize, cn as usize);
                if rn >= m || cn >= n { continue; }
                if grid[rn][cn] == 0 { continue; }
                result[*i].1.push(*hm.get(&(rn, cn)).unwrap());
            }
        }
        result
    }

    /// Finds the maximum amount of gold that can be collected by starting from any cell in the given grid.
    ///
    /// The function constructs a graph from the grid and then performs a depth-first search on the graph to find the maximum amount of gold.
    ///
    /// # Arguments
    ///
    /// * `grid` - A vector of vectors of i32. Each inner vector represents a row in the grid.
    ///
    /// # Returns
    ///
    /// * An i32, which is the maximum amount of gold that can be collected.
    pub fn get_maximum_gold(grid: Vec<Vec<i32>>) -> i32 {
        let g = Self::construct_graph(grid);
        let n = g.len();
        assert!(n < 32);
        let total = g.iter().map(|(v, _)| *v).sum::<i32>();
        let mut result = 0;
        for start in 0..n {
            let mut wq = Vec::new();
            wq.push((start, 0, 0));
            while let Some((i, cur, mask)) = wq.pop() {
                let cur = cur + g[i].0;
                let mask = mask | (1 << i);
                for ni in g[i].1.iter() {
                    if mask & (1 << *ni) == 0 {
                        wq.push((*ni, cur, mask));
                    }
                }
                result = result.max(cur);
                if result == total { break; }
            }
        }

        result
    }
}
