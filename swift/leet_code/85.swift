// Importing Foundation for basic Swift functionalities
import Foundation

/**
 This class provides a solution for finding the maximal rectangle in a binary matrix.

 The `maximalRectangle` function takes a 2D matrix of characters as input, where each character is either '0' or '1'.
 It returns the area of the largest rectangle containing only '1's in the matrix.

 The `largestRectangleArea` function is a helper function that calculates the largest rectangle area in a histogram.
 It takes an array of integers as input, where each integer represents the height of a bar in the histogram.
 It returns the area of the largest rectangle that can be formed in the histogram.
 */
class Solution {
    func maximalRectangle(_ matrix: [[Character]]) -> Int {
        // Initialize the histograms and heightAtColums arrays
        var histograms = Array(repeating: Array(repeating: 0, count: matrix.first?.count ?? 0), count: matrix.count)
        var heightAtColums = [Int: Int]()

        // Iterate over the matrix to calculate the height of '1's at each column
        for row in 0..<matrix.count {
            for column in 0..<matrix[row].count {
                let height = matrix[row][column]
                if height == "1" {
                    heightAtColums[column] = (heightAtColums[column] ?? 0) + 1
                } else {
                    heightAtColums[column] = 0
                }
                histograms[row][column] = heightAtColums[column] ?? 0
            }
        }

        // Initialize the maxArea to the smallest possible integer
        var maxArea = Int.min

        // Iterate over the histograms to calculate the largest rectangle area
        for histogram in histograms {
            let area = largestRectangleArea(histogram)
            maxArea = max(area, maxArea)
        }

        // Return the maxArea
        return maxArea
    }

    func largestRectangleArea(_ heights: [Int]) -> Int {
        // Initialize the stack and maxArea
        var stack = [Int]()
        var maxArea = 0
        var i = 0

        // Iterate over the heights to calculate the largest rectangle area
        while i < heights.count {
            if stack.isEmpty || heights[i] >= heights[stack.last ?? 0] {
                stack.append(i)
                i += 1
            } else {
                let top = stack.removeLast()
                let width = stack.isEmpty ? i : i - stack.last! - 1
                maxArea = max(maxArea, heights[top] * width)
            }
        }

        // Continue to calculate the largest rectangle area with the remaining heights in the stack
        while !stack.isEmpty {
            let top = stack.removeLast()
            let width = stack.isEmpty ? i : i - stack.last! - 1
            maxArea = max(maxArea, heights[top] * width)
        }

        // Return the maxArea
        return maxArea
    }
}
