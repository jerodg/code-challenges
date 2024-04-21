/// This module provides a solution for the trapping rainwater problem.
///
/// It includes a function `trap` that calculates the amount of rainwater that can be trapped
/// given a list of heights.
use std::cmp;

impl Solution {
    /// Calculate the amount of rainwater that can be trapped given a list of heights.
    ///
    /// # Arguments
    ///
    /// * `height` - A vector of i32s representing the heights.
    ///
    /// # Returns
    ///
    /// * An i32 representing the amount of trapped rainwater.
    pub fn trap(height: Vec<i32>) -> i32 {
        // Initialize peak index
        let mut peak_i = 0;
        let mut i = 1;
        // Find the peak of the height
        loop {
            if i == height.len() {
                break;
            }
            if height[i] > height[peak_i] {
                peak_i = i;
            }
            i += 1;
        }

        // Initialize water and left_max
        let mut water = 0;
        let mut i = 0;
        let mut left_max = height[0];
        // Calculate water trapped on the left side of the peak
        loop {
            if i == peak_i {
                break;
            }
            if height[i] > left_max {
                left_max = height[i];
            }
            water += left_max - height[i];
            i += 1;
        }

        // Initialize right_max
        let mut i = height.len() - 1;
        let mut right_max = height[i];
        // Calculate water trapped on the right side of the peak
        loop {
            if i == peak_i {
                return water;
            }
            if height[i] > right_max {
                right_max = height[i];
            }
            water += right_max - height[i];
            i -= 1;
        }
    }
}
