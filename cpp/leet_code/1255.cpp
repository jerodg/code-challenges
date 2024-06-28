/**
 * Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
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
 * program. If not, see SSPL.
 */

/**
 * @file 1255.cpp
 * @brief This file contains the implementation of the Solution class which is used to solve the problem of maximizing the score of words.
 * @package leet_code
 */

#pragma GCC optimize("O3", "unroll-loops") // Compiler directive for optimization

#include <string>
#include <vector>

/**
 * @class Solution
 * @brief This class provides a solution to the problem of maximizing the score of words.
 *
 * It contains two public methods: solve and maxScoreWords.
 */
class Solution {
public:
    /**
     * @brief This method is a recursive function that calculates the maximum score that can be obtained from the words.
     *
     * @param i The current index in the words vector.
     * @param n The total number of words.
     * @param mp A vector representing the frequency of each letter.
     * @param score A vector representing the score of each letter.
     * @param ans The current maximum score.
     * @param sum The current sum of scores.
     * @param words The vector of words.
     *
     * This method does not return a value, but modifies the ans variable to hold the maximum score.
     */
    static void solve(const int i, int& n, std::vector<int>& mp, std::vector<int>& score, int& ans, const int sum, std::vector<std::string>& words){
        ans = std::max(ans, sum); // Update the maximum score

        if(i >= n) return ; // Base case of recursion

        std::vector<int> temp_map = mp; // Copy of the frequency map

        int j = 0; // Index for iterating over the characters of the current word
        int sum2 = 0; // Sum of scores of the characters of the current word

        // Iterate over the characters of the current word
        for(j = 0; j < words[i].length(); j++){
            temp_map[words[i][j] - 'a']--; // Decrease the frequency of the current character
            sum2+= score[words[i][j] - 'a']; // Add the score of the current character to sum2
            if(temp_map[words[i][j]-'a'] < 0) break; // If the frequency of the current character is negative, break the loop
        }

        // If all characters of the current word were used
        if( j == words[i].length()){
            solve(i+1, n, temp_map, score, ans, sum + sum2, words); // Recursive call with the updated frequency map and sum
        }
        solve(i+1, n, mp, score, ans, sum, words); // Recursive call without using the current word
    }

    /**
     * @brief This method calculates the maximum score that can be obtained from the words.
     *
     * @param words A vector of words.
     * @param letters A vector of letters.
     * @param score A vector of scores for each letter.
     * @return The maximum score.
     *
     * This method uses the solve method to calculate the maximum score.
     */
    static int maxScoreWords(std::vector<std::string>& words, std::vector<char>& letters, std::vector<int>& score) {
        std::vector<int> mp(26, 0); // Frequency map for the letters
        for(const char i : letters){
            mp[i - 'a']++; // Increase the frequency of the current letter
        }
        int ans = 0; // Maximum score
        int n = words.size(); // Number of words
        solve(0, n, mp, score, ans, 0, words); // Call the solve method to calculate the maximum score
        return ans; // Return the maximum score
    }
};
