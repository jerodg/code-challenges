/**
# LeetCode Problem 2370 Solution
This module provides a solution for the LeetCode problem 2370. The problem is about finding the longest ideal string.

The `Solution` class contains a single method `longestIdealString(_:_:)` which calculates the longest ideal string.

- Note: This module does not handle any errors as the problem constraints from LeetCode ensures the inputs are always valid.
*/

class Solution {
    /**
    Calculates the longest ideal string.

    This function takes a string `s` and an integer `k` as input. It calculates the longest ideal string by iterating over each character in the string and updating a dynamic programming array `dp`. The `dp` array stores the longest ideal string that can be formed with each character as the last character.

    - Parameters:
       - s: The input string. It is a string of lowercase English letters.
       - k: The maximum difference in ASCII values between any two characters in the ideal string. It is a non-negative integer.

    - Returns: The length of the longest ideal string. It is a non-negative integer.

    - Complexity: This function runs in O(n) time where n is the length of the string `s`. It uses O(1) extra space.
    */
    func longestIdealString(_ s: String, _ k: Int) -> Int {
        // Initialize the dynamic programming array
        var dp = [Int](repeating: 0, count: 26)
        let a = Character("a").asciiValue!

        // Iterate over each character in the string
        for (i, c) in s.enumerated() {
            let ci = Int(c.asciiValue! - a)
            var best = 1

            // Find the best value for the current character
            for oc in max(0, ci-k)...min(ci+k, 25) {
                best = max(best, dp[oc] + 1)
            }

            // Update the dynamic programming array
            dp[ci] = best
        }

        // Return the maximum value in the dynamic programming array
        return dp.max()!
    }
}
