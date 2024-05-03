// This module provides a solution to a problem related to finding wonderful
// substrings. The problem is solved using bit manipulation and array
// operations. The main class in this module is `Solution` which provides a
// static method `wonderfulSubstrings`.

#pragma GCC optimize("O3", "unroll-loops")
#include <execution>
#include <iostream>

// This lambda function is used to initialize the standard input and output
// streams. It sets the synchronization of the standard streams with their
// respective C streams to `false`, and unties the tied streams of `cin` and
// `cout`. It returns a character 'c' after performing these operations.
auto init = []() {
  std::ios::sync_with_stdio(false);
  std::cin.tie(nullptr);
  std::cout.tie(nullptr);
  return 'c';
}();

class Solution {
public:
  // This static method calculates the number of wonderful substrings in a given
  // word. A wonderful substring is defined as a substring where at most one
  // character appears an odd number of times. The method uses bit manipulation
  // and array operations to solve the problem.
  //
  // Parameters:
  // - `word` (const std::string&): The input word in which to find the
  // wonderful substrings.
  //
  // Returns:
  // - `long long`: The number of wonderful substrings in the input word.
  static long long wonderfulSubstrings(const std::string &word) {
    // An array to store the count of substrings for each bitmask.
    std::array<uint16_t, 1024> cnt_by_mask{};
    cnt_by_mask.fill(0);
    cnt_by_mask[0] = 1;
    int bitmask = 0;
    // Iterate over each character in the word.
    for (const char ch : word) {
      // Update the bitmask and increment the count for the current bitmask.
      ++cnt_by_mask[bitmask ^= (1 << (ch - 'a'))];
    }
    // An array of mask differences that are considered okay.
    constexpr std::array<int, 10> ok_mask_differences = {
        1, 2, 4, 8, 0x10, 0x20, 0x40, 0x80, 0x100, 0x200};
    int64_t ans = 0;
    // Iterate over each possible mask.
    for (int mask = 0; mask < 1024; ++mask) {
      const auto cnt_this_mask = cnt_by_mask[mask];
      // Add the number of pairs of substrings with the same bitmask to the
      // answer.
      ans += static_cast<int64_t>(cnt_this_mask) * (cnt_this_mask - 1) / 2;
      int num_other_ok_mask_endpoints = 0;
      // Iterate over each okay mask difference.
      for (const auto diff : ok_mask_differences) {
        if (const auto ok_mask = mask ^ diff; mask < ok_mask) {
          // Count the number of substrings with a bitmask that differs from the
          // current mask by an okay difference.
          num_other_ok_mask_endpoints += cnt_by_mask[ok_mask];
        }
      }
      // Add the number of substrings with a bitmask that differs from the
      // current mask by an okay difference to the answer.
      ans += static_cast<int64_t>(cnt_this_mask) * num_other_ok_mask_endpoints;
    }
    // Return the total number of wonderful substrings.
    return ans;
  }
};
