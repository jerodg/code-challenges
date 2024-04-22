// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <vector>  // Include for vector
#include <stack>   // Include for stack
#include <algorithm>  // Include for max function

// Class to solve the problem of finding the maximal rectangle in a matrix
class Solution {
public:
    // Function to find the largest rectangle area in a histogram
    // @param histo: a vector of integers representing the histogram
    // @return: the maximum area of the rectangle in the histogram
    int largestRectangleArea(std::vector<int>& histo) {
        std::stack<int> st;
        int maxA = 0;
        int n = histo.size();
        for (int i = 0; i <= n; i++) {
            // Pop the stack while the current height is less than the top of the stack
            while (!st.empty() && (i == n || histo[st.top()] >= histo[i])) {
                int height = histo[st.top()];
                st.pop();
                int width;
                // If the stack is empty, the width is the current index
                // Otherwise, the width is the difference between the current index and the new top of the stack
                if (st.empty())
                    width = i;
                else
                    width = i - st.top() - 1;
                // Update the maximum area
                maxA = std::max(maxA, width * height);
            }
            st.push(i);
        }
        return maxA;
    }

    // Function to solve the problem of finding the maximal rectangle in a matrix
    // @param mat: a matrix of characters
    // @param n: the number of rows in the matrix
    // @param m: the number of columns in the matrix
    // @return: the area of the maximal rectangle
    int solve(std::vector<std::vector<char>>& mat, int n, int m) {
        int maxArea = 0;
        std::vector<int> height(m, 0);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // If the current cell is '1', increase the height
                // Otherwise, reset the height
                if (mat[i][j] == '1') height[j]++;
                else height[j] = 0;
            }
            // Calculate the area of the largest rectangle in the current histogram
            int area = largestRectangleArea(height);
            // Update the maximum area
            maxArea = std::max(area, maxArea);
        }

        return maxArea;
    }

    // Function to find the maximal rectangle in a matrix
    // @param matrix: a matrix of characters
    // @return: the area of the maximal rectangle
    int maximalRectangle(std::vector<std::vector<char>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();

        return solve(matrix, n, m);
    }
};
