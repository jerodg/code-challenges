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
 * @file 140.cpp
 * @brief This file contains the implementation of the Solution class which is used to solve the problem of word breaking.
 * @package leet_code
 */

#include <string>
#include <unordered_map>
#include <vector>

/**
 * @class Solution
 * @brief This class provides a solution to the problem of word breaking.
 *
 * It contains two public methods: solve and wordBreak.
 */
class Solution {
public:

    /**
     * @brief This vector stores the final answers.
     */
    std::vector<std::string> ans;

    /**
     * @brief This method is a recursive function that constructs all possible sentences from the given string.
     *
     * @param i The current index in the given string.
     * @param sentence The current sentence being constructed.
     * @param given_string The string from which sentences are to be constructed.
     * @param does_exist A map that checks if a word exists in the dictionary or not.
     *
     * This method does not return a value, but modifies the ans vector to hold all possible sentences.
     */
    void solve(const int i, std::string &sentence, std::string &given_string, std::unordered_map<std::string, bool> &does_exist) {
        if (i >= given_string.size()) {
            ans.push_back(sentence);
            return;
        }

        for (int j = i + 1; j <= i + 10  &&  j <= given_string.size(); j++) {
            if (std::string word = given_string.substr(i, j - i);does_exist.contains(word)  ) {
                if (sentence.empty()) {
                    sentence = word;
                } else {
                    sentence += " " + word;
                }
                solve(j, sentence, given_string, does_exist);
                int x = 0;
                while (x < word.size()) {
                    x++;
                    sentence.pop_back();
                }

                if (!sentence.empty()) {
                    sentence.pop_back();
                }
            }
        }
    }

    /**
     * @brief This method returns all possible sentences that can be formed from the given string using the words in the dictionary.
     *
     * @param s The string from which sentences are to be constructed.
     * @param wordDict The dictionary of words.
     * @return A vector of all possible sentences.
     *
     * This method uses the solve method to construct all possible sentences.
     */
    std::vector<std::string> wordBreak(std::string s, std::vector<std::string>& wordDict) {
        std::string sentence;
        std::unordered_map<std::string, bool> doesExist;
        for (const auto& x: wordDict) {
            doesExist[x] = true;
        }

        ans.clear();
        solve(0, sentence, s, doesExist);
        return ans;
    }
};
