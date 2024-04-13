using System;
using System.Collections.Generic;

/// <summary>
/// This module contains a solution for calculating the largest rectangle in a matrix.
/// </summary>
public class Solution {
    /// <summary>
    /// Calculates the largest rectangle that can be formed in a histogram.
    /// </summary>
    /// <param name="heights">An array of integers representing the histogram.</param>
    /// <returns>The area of the largest rectangle that can be formed in the histogram.</returns>
    public int LargestRectangleArea(int[] heights) {
        // Stack to store the indices of the bars in the histogram
        Stack<int> st = new Stack<int>();
        st.Push(-1);
        int n = heights.Length;
        
        int maxArea = 0;
        
        // Iterate over each bar in the histogram
        for (int i=0; i<n; i++)
        {
            // While the current bar is shorter than the bar at the top of the stack
            while (st.Peek() != -1 && heights[st.Peek()] >= heights[i])
            {
                // Calculate the area of the rectangle that can be formed using the bar at the top of the stack as the shortest bar
                int cHeight = heights[st.Pop()];
                int cWidth = i-st.Peek()-1;
                maxArea = Math.Max(cHeight*cWidth, maxArea);
            }
            // Push the current bar to the stack
            st.Push(i);
        }
        
        // Calculate the area of the remaining rectangles
        while (st.Peek() != -1)
        {
            int cHeight = heights[st.Pop()];
            int cWidth = n-st.Peek()-1;
            maxArea = Math.Max(cHeight*cWidth, maxArea);
        }
        return maxArea;
    }
    
    /// <summary>
    /// Calculates the largest rectangle that can be formed in a matrix.
    /// </summary>
    /// <param name="matrix">A 2D array of characters representing the matrix.</param>
    /// <returns>The area of the largest rectangle that can be formed in the matrix.</returns>
    public int MaximalRectangle(char[][] matrix) {
        int rows = matrix.Length;
        int cols = matrix[0].Length;
        // Array to store the heights of the bars in the histogram
        int[] heights = new int[cols];
        
        int maxArea = 0;
        
        // Iterate over each row in the matrix
        for (int i=0; i<rows; i++)
        {
            // Iterate over each column in the matrix
            for (int j=0; j<cols; j++)
            {
                // Update the height of the bar at the current column
                heights[j] = matrix[i][j] == '0' ? 0 : heights[j] + matrix[i][j] - '0';
            }
            // Calculate the largest rectangle that can be formed in the histogram
            maxArea = Math.Max(maxArea, LargestRectangleArea(heights));
        }
        return maxArea;
    }
}