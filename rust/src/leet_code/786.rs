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
// The main method in this file is `kth_smallest_prime_fraction` which calculates the Kth smallest prime fraction.

/// The Solution struct does not hold any data and is only used to group related methods.
pub struct Solution {}

impl Solution {
    /// This method calculates the Kth smallest prime fraction from a given list of sorted primes.
    ///
    /// # Parameters
    ///
    /// * `arr`: A vector of sorted prime numbers.
    /// * `k`: The Kth smallest prime fraction to find.
    ///
    /// # Returns
    ///
    /// A vector containing the numerator and denominator of the Kth smallest prime fraction.
    ///
    /// # Example
    ///
    /// ```
    /// let arr = vec![1, 2, 3, 5];
    /// let k = 3;
    /// let result = Solution::kth_smallest_prime_fraction(arr, k);
    /// assert_eq!(result, vec![2, 5]);
    /// ```
    pub fn kth_smallest_prime_fraction(arr: Vec<i32>, k: i32) -> Vec<i32> {
        // The length of the input array
        let n = arr.len();
        // The lower and upper bounds for the binary search
        let mut l = 0.0;
        let mut r = 1.0;
        // The answer to be returned
        let mut ans = vec![0, 1];
        // The binary search
        while r - l > f64::EPSILON {
            let mid = (l + r) / 2.0;
            // The numerator and denominator of the current fraction
            let mut p = 0;
            let mut q = 1;
            // The count of fractions less than or equal to mid
            let mut cnt = 0;
            // The index for the inner loop
            let mut j = 1;
            // The outer loop
            for i in 0..n {
                // The inner loop
                while j < n && arr[i] as f64 / arr[j] as f64 > mid {
                    j += 1;
                }
                // If the inner loop didn't reach the end of the array
                if j < n {
                    // Increase the count by the number of fractions less than or equal to mid
                    cnt += n - j;
                    // If the current fraction is smaller than the previous smallest fraction
                    if p * arr[j] < q * arr[i] {
                        // Update the smallest fraction
                        p = arr[i];
                        q = arr[j];
                    }
                }
            }
            // If the count is equal to k
            if cnt as i32 == k {
                // Update the answer and break the loop
                ans[0] = p;
                ans[1] = q;
                break;
                // If the count is less than k
            } else if (cnt as i32) < k {
                // Update the lower bound
                l = mid;
                // If the count is greater than k
            } else {
                // Update the upper bound
                r = mid;
            }
        }
        // Return the answer
        ans
    }
}
