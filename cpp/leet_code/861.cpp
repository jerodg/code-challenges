/**
 * @file 861.cpp
 * @brief This file contains the implementation of a solution for a problem related to flipping a binary matrix to maximize its score.
 * @details The matrix is represented as a 2D vector. Each row in the matrix represents a binary number and the goal is to maximize the sum of these numbers.
 * The solution uses a greedy approach to flip the rows and columns of the matrix to maximize the score.
 *
 * @copyright Copyright ©2012-2024 Jerod Gawne <https://github.com/jerodg/>
 *
 * This program is free software: you can redistribute it and/or modify it under
 * the terms of the Server Side Public License (SSPL) as published by MongoDB,
 * Inc., either version 1 of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the SSPL for more details.
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software. You should have received
 * a copy of the SSPL along with this program. If not, see
 * <https://www.mongodb.com/licensing/server-side-public-license>.
 */

#include <vector>

/**
 * @class Solution
 * @brief This class encapsulates the solution for the problem.
 */
class Solution {
public:
    /**
     * @brief This function calculates the maximum score that can be obtained by flipping the rows and columns of the binary matrix.
     * @param grid A reference to the 2D vector representing the binary matrix.
     * @return The maximum score that can be obtained.
     */
    int matrixScore(std::vector<std::vector<int>>& grid) {
        const int m=grid.size(); // The number of rows in the matrix.
        const int n=grid[0].size(); // The number of columns in the matrix.

        // Flip the rows of the matrix such that the first element of each row is 1.
        for(int i=0;i<m;i++){
            if(grid[i][0]==0){
                for(int j=0;j<n;j++){
                    grid[i][j]=1-grid[i][j];
                }
            }
        }

        // Flip the columns of the matrix such that the number of 1s in each column is maximized.
        for(int j=1;j<n;j++){
            int cnt0=0,cnt1=0;
            for(int i=0;i<m;i++){
                if(grid[i][j]==0) cnt0++;
                else cnt1++;
            }
            if(cnt0 > cnt1) {
                for(int i=0;i<m;i++){
                    grid[i][j]=1-grid[i][j];
                }
            }
        }

        // Calculate the score of the matrix.
        int ans=0;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                const int colscore= grid[i][j] << (n-j-1);
                ans+=colscore;
            }
        }
        return ans;
    }
};
