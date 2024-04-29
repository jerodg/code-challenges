/**
# LeetCode 1289 Solution
This module provides a solution for the LeetCode problem 1289, "Minimum Falling Path Sum II". The problem is about finding the minimum sum of a falling path through a given grid. A falling path starts at any element in the first row and chooses the element in the next row which is not in the same column as the current element.

The `Solution` class contains two methods:
- `getTwoMin(_:)` which returns the two smallest numbers in a given row and the index of the smallest number.
- `minFallingPathSum(_:)` which calculates the minimum falling path sum in a given grid.

This module does not handle any errors as it assumes that the input is always a valid grid.

- Note: This module does not modify the input grid.
*/

class Solution {
    /**
    This method returns the two smallest numbers in a given row and the index of the smallest number.

    - Parameters:
       - row: An array of integers representing a row in the grid.

    - Returns: A tuple containing the smallest number, its index, and the second smallest number in the row.

    - Complexity: This method runs in O(n) time where n is the number of elements in the row.
    */
    private func getTwoMin(_ row: [Int]) -> (Int, Int, Int) {
        var (min1, except, min2) = (Int.max, 0, Int.max)

        for (num, i) in row.enumerated() {
            if i < min1 {
                min2 = min1
                min1 = i
                except = num
            } else if i < min2 {
                min2 = i
            }
        }

        return (min1, except, min2)
    }

    /**
    This method calculates the minimum falling path sum in a given grid.

    - Parameters:
       - grid: A 2D array of integers representing the grid.

    - Returns: The minimum falling path sum as an integer.

    - Complexity: This method runs in O(n^2) time where n is the number of rows in the grid.
    */
    func minFallingPathSum(_ grid: [[Int]]) -> Int {
        var resulting: [[Int]] = grid
        var n = grid.count

        for j in 0 ..< n - 1 {
            let (min1, except, min2) = getTwoMin(resulting[j])

            for i in 0 ..< n {
                resulting[j + 1][i] += except == i ? min2 : min1
            }
        }

        return resulting.last!.min()!
    }
}
