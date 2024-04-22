/**
 * @file 1249.cpp
 * @brief Contains the implementation of the Solution class.
 *
 * This file contains the implementation of a Solution class which provides a method to make a string valid by removing the minimum number of parentheses.
 */
// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <string>

/**
 * @class Solution
 * @brief A class providing a method to make a string valid by removing the minimum number of parentheses.
 *
 * This class provides a method to make a string valid by removing the minimum number of parentheses. The method iterates over the string, counts the parentheses and removes the invalid ones.
 */
class Solution {
public:
    /**
     * @brief Makes a string valid by removing the minimum number of parentheses.
     *
     * This method makes a string valid by removing the minimum number of parentheses. It iterates over the string, counts the parentheses and removes the invalid ones.
     *
     * @param s The string to make valid.
     * @return The valid string.
     *
     * @throws std::out_of_range If the string index is out of range.
     */
    static std::string minRemoveToMakeValid(std::string s) {
        int count = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                count++;
            } else if (s[i] == ')') {
                count--;
            }
            if (count < 0) {
                s.erase(i, 1);
                i--;
                count++;
            }
        }
        if (count == 0) {
            return s;
        }
        int j = s.size() - 1;
        while (j >= 0 && count > 0) {
            if (s[j] == '(') {
                s.erase(j, 1);
                count--;
            }
            j--;
        }
        return s;
    }
};
