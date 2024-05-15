/**
 * @file leet_code/861.c
 * @brief This file contains the implementation of a function to compute the score of a binary matrix after flipping.
 *
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */

#pragma GCC optimize("O3", "unroll-loops")

#include <stdint.h>
#include <string.h>

/**
 * @brief Computes the score of a binary matrix after flipping.
 *
 * The function flips each row of the matrix so that the leftmost bit of each row is 1. Then, it flips columns to maximize the number of 1s.
 * The score of the matrix is the sum of the binary numbers represented by each row.
 *
 * @param grid The 2D binary matrix.
 * @param r The number of rows in the matrix.
 * @param gridColSize The number of columns in the matrix.
 * @return int The score of the matrix after flipping.
 */
int matrixScore(int** grid, int r, const int* gridColSize) {
    const int c = *gridColSize;

    // Array to store the number of 1s in each column
    uint8_t col1[c];
    memset(col1, 0, sizeof(col1));

    // Variable to store the sum of the binary numbers represented by each row
    int sum = 0;

    // Loop through each row
    for (register int i = 0; i < r; i++) {
        int x = 0;
        bool one;

        // Loop through each column
        for (register int j = 0; j < c; j++) {
            // Flip the bit if the leftmost bit of the row is 0
            one = (grid[i][0] == 0) ^ (grid[i][j] == 1);

            // Compute the binary number represented by the row
            x = (x << 1) + one;

            // Update the number of 1s in the column
            col1[j] += one;
        }

        // Add the binary number represented by the row to the sum
        sum += x;
    }

    // Loop through each column
    for (register int i = 0; i < c; i++) {
        // If the number of 1s in the column is more than half the number of rows, do not flip the column
        if (col1[i] > r / 2) {
            continue;
        }

        // Otherwise, flip the column and update the sum
        sum += (1 << (c - 1 - i)) * (r - 2 * col1[i]);
    }

    return sum;
}
