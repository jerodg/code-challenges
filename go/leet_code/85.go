// Package leet_code provides solutions for LeetCode problems.
package leet_code

// maximalRectangle calculates the largest rectangle that can be filled with '1's in the given matrix.
// The function uses a dynamic programming approach where it calculates the maximum area of the rectangle
// at each cell of the matrix. The area is calculated based on the height and width (left and right boundaries)
// of the rectangle that can be formed at each cell.
//
// Parameters:
//  - matrix: A 2D byte array where '1's represent filled cells and '0's represent empty cells.
//
// Returns:
//  - The area of the largest rectangle that can be filled with '1's.
func maximalRectangle(matrix [][]byte) int {
	// m and n represent the number of rows and columns in the matrix respectively.
	m, n := len(matrix), len(matrix[0])

	// heights, left, and right are arrays that store the height of the rectangle and the left and right boundaries of the rectangle at each column.
	heights := make([]int, n)
	left := make([]int, n)
	right := make([]int, n)

	// Initialize the right boundaries to the number of columns in the matrix.
	for j := 0; j < n; j++ {
		right[j] = n
	}

	// max stores the maximum area of the rectangle found so far.
	max := 0

	// Iterate over each cell in the matrix.
	for i := 0; i < m; i++ {
		// leftest and rightest store the leftmost and rightmost boundaries of the rectangle at the current row.
		leftest, rightest := 0, n - 1

		// Iterate over each column in the current row.
		for j := 0; j < n; j++ {
			// If the current cell is filled ('1'), update the height and left boundary of the rectangle at the current column.
			if matrix[i][j] == '1' {
				heights[j]++
				if leftest > left[j] {
					left[j] = leftest
				}
			} else {
				// If the current cell is empty ('0'), reset the height and left boundary of the rectangle at the current column and update leftest.
				heights[j] = 0
				left[j] = 0
				leftest = j + 1
			}

			// Update the right boundary of the rectangle at the current column from the right side of the row.
			if matrix[i][n-1-j] == '1' {
				if rightest < right[n-1-j] {
					right[n-1-j] = rightest
				}
			} else {
				right[n-1-j] = n
				rightest = n - 1 - j - 1
			}
		}

		// Calculate the area of the rectangle at each column and update max if a larger area is found.
		for j := 0; j < n; j++ {
			area := (right[j] - left[j] + 1) * heights[j]
			if area > max {
				max = area
			}
		}
	}

	// Return the maximum area of the rectangle found.
	return max
}
