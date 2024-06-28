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
 * @file leet_code/2597.cpp
 * @brief This file contains the Solution class which is used to solve the problem of finding beautiful subsets.
 *
 * Package leet_code
 */

#include <map>
#include <vector>

/**
 * @class Solution
 * @brief This class is used to solve the problem of finding beautiful subsets.
 *
 * A beautiful subset is defined as a subset of an array where the difference between any two elements is equal to a given difference.
 */
class Solution {
private:
    /**
     * @brief This method is used to count the number of beautiful subsets in a given array.
     *
     * @param subsets A vector of pairs, where each pair represents a subset.
     * @param num_subsets The total number of subsets.
     * @param difference The difference between any two elements in a beautiful subset.
     * @param i The current index in the subsets vector.
     * @param counts A vector to store the count of beautiful subsets for each index.
     * @return The count of beautiful subsets.
     */
    static int count_beautiful_subsets(std::vector<std::pair<int, int>>& subsets, const int num_subsets, const int difference,
        const int i, std::vector<int>& counts) {
        if (i == num_subsets) {
            return 1;
        }

        if (counts[i] != -1) {
            return counts[i];
        }

        // Count the beautiful subsets when the current subset is skipped
        const int skip = count_beautiful_subsets(subsets, num_subsets, difference, i + 1, counts);

        // Count the beautiful subsets when the current subset is taken
        int take = (1 << subsets[i].second) - 1;

        // If the next subset is a beautiful subset with the current subset, multiply the count
        if (i + 1 < num_subsets && subsets[i + 1].first - subsets[i].first == difference) {
            take *= count_beautiful_subsets(subsets, num_subsets, difference, i + 2, counts);
        } else {
            take *= count_beautiful_subsets(subsets, num_subsets, difference, i + 1, counts);
        }

        // Store the count of beautiful subsets for the current index
        return counts[i] = skip + take;
    }

public:
    /**
     * @brief This method is used to find the total number of beautiful subsets in a given array.
     *
     * @param nums The given array.
     * @param difference The difference between any two elements in a beautiful subset.
     * @return The total number of beautiful subsets.
     */
    static int beautifulSubsets(std::vector<int>& nums, const int difference) {
        int tot_count = 1;
        // A map to store the frequency of each number modulo the difference
        std::map<int, std::map<int, int>> freq_map;

        // Populate the frequency map
        for (int& num: nums) {
            freq_map[num % difference][num]++;
        }

        // For each unique number modulo the difference, count the beautiful subsets
        for (auto& fr: freq_map) {
            std::vector<std::pair<int, int>> subsets(fr.second.begin(), fr.second.end());
            std::vector<int> counts(subsets.size(), -1);
            tot_count *= count_beautiful_subsets(subsets, subsets.size(), difference, 0, counts);
        }
        return tot_count - 1;
    }
};
