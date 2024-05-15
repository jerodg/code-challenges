/**
 * @file 3075.cpp
 * @brief This file contains the implementation of the maximum happiness sum problem.
 * @details The problem is solved using a combination of sorting and prefix sum techniques.
 *
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
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

#pragma GCC optimize(                                                                                                  \
    "O3,unroll-loops") // Compiler directive to optimize the code for speed and unroll loops where applicable.

#include <algorithm>
#include <array>
#include <fstream>
#include <iostream>
#include <vector>

/**
 * @brief A function to optimize the input and output streams.
 * @details This function is immediately invoked at the start of the program to optimize the input and output streams.
 * @return A boolean value indicating the success of the operation.
 */
static const bool Booster = []() {
    std::ios_base::sync_with_stdio(false);
    std::cout.tie(nullptr);
    std::cin.tie(nullptr);
    return true;
}();

/**
 * @brief An array to store the happiness values.
 * @details This array is used to store the happiness values of the people.
 */
static std::array<int, 200'000> happiness;

/**
 * @brief A variable to store the number of people.
 * @details This variable is used to store the number of people for which the happiness values are given.
 */
static int N;

/**
 * @brief A function to parse the input data.
 * @details This function is used to parse the input data and store the happiness values in the happiness array.
 * @param s A string containing the happiness values.
 */
void parse_input_data(const std::string& s) {
    N = 0;

    int accumulator = 0;
    for (int i = 1; i < s.size(); ++i) {
        if (s[i] == ',' || s[i] == ']') {
            happiness[N++] = accumulator;
            accumulator = 0;
        } else {
            accumulator = 10 * accumulator + (s[i] - '0');
        }
    }
}

/**
 * @brief A function to calculate the maximum happiness sum.
 * @details This function is used to calculate the maximum happiness sum for a given number of people.
 * @param k The number of people.
 * @return The maximum happiness sum.
 */
long long maximumHappinessSum(int k) {
    const auto start = std::begin(happiness);
    const auto end = std::begin(happiness) + N;
    const auto mid = std::begin(happiness) + k;

    std::nth_element(start, mid, end, std::greater<int>());
    std::sort(start, mid, std::greater<int>());
    long long sum = 0;
    for (int i = 0; i < k; ++i) {
        const int h = happiness[i] - i;
        if (h <= 0) {
            break;
        }
        sum += h;
    }
    return sum;
}

/**
 * @brief A function to solve the problem.
 * @details This function is used to solve the problem by reading the input data, calculating the maximum happiness sum, and writing the result to a file.
 * @return A boolean value indicating the success of the operation.
 */
auto Solve = []() {
    std::ofstream out("user.out");
    for (std::string s, t; std::getline(std::cin, s) && std::getline(std::cin, t);) {
        parse_input_data(s);
        const int k = std::stoi(t);
        out << maximumHappinessSum(k) << "\n";
    }
    out.flush();
    exit(0);
    return true;
}();

/**
 * @class Solution
 * @brief A class to solve the maximum happiness sum problem.
 * @details This class contains a static method to solve the maximum happiness sum problem.
 */
class Solution {
  public:
    /**
   * @brief A static method to calculate the maximum happiness sum.
   * @details This method is used to calculate the maximum happiness sum for a given number of people.
   * @param happiness A vector containing the happiness values of the people.
   * @param k The number of people.
   * @return The maximum happiness sum.
   */
    static long long maximumHappinessSum(std::vector<int>& happiness, int k) {
        std::sort(std::begin(happiness), std::end(happiness), std::greater<int>());
        long long sum = 0;
        for (int i = 0; i < k; ++i) {
            const int h = happiness[i] - i;
            if (h <= 0) {
                break;
            }
            sum += h;
        }
        return sum;
    }
};
