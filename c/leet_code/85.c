#include <stdlib.h>
/**
 * Function to calculate the maximal rectangle in a matrix.
 * The matrix is represented as a 2D array of characters where '1' represents a filled cell and '0' represents an empty cell.
 * The function uses dynamic programming to calculate the maximal rectangle.
 *
 * @param matrix: A 2D array of characters representing the matrix.
 * @param rowSize: The number of rows in the matrix.
 * @param colSize: A pointer to the number of columns in the matrix.
 * @return The area of the maximal rectangle.
 */
int maximalRectangle(char** matrix, int rowSize, int* colSize) {
    // If the matrix is empty, return 0
    if (rowSize == 0 || *colSize == 0) {
        return 0;
    }

    // Allocate memory for height, left, and right arrays
    int* height = (int*)malloc(sizeof(int) * (*colSize));
    int* left = (int*)malloc(sizeof(int) * (*colSize));
    int* right = (int*)malloc(sizeof(int) * (*colSize));
    int count = 0;

    // Initialize height, left, and right arrays
    for (int i = 0; i < *colSize; i++) {
        height[i] = 0;
        left[i] = 0;
        right[i] = *colSize;
    }

    // Iterate over each row in the matrix
    for (int i = 0; i < rowSize; i++) {
        int currentLeft = 0, currentRight = *colSize;

        // Update height and left for each column
        for (int j = 0; j < *colSize; j++) {
            if (matrix[i][j] == '1') {
                height[j]++;
                left[j] = left[j] > currentLeft ? left[j] : currentLeft;
            } else {
                height[j] = 0;
                left[j] = 0;
                currentLeft = j + 1;
            }
        }

        // Update right for each column
        for (int j = *colSize - 1; j >= 0; j--) {
            if (matrix[i][j] == '1') {
                right[j] = right[j] < currentRight ? right[j] : currentRight;
            } else {
                right[j] = *colSize;
                currentRight = j;
            }
        }

        // Calculate the maximal rectangle
        for (int j = 0; j < *colSize; j++) {
            count = count > (right[j] - left[j]) * height[j] ? count : (right[j] - left[j]) * height[j];
        }
    }

    // Free the allocated memory
    free(height);
    free(left);
    free(right);

    return count;
}
