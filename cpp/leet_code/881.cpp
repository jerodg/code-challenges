// This module provides a solution to the problem of determining the minimum
// number of rescue boats required to save all people given a weight limit for
// each boat. The problem is solved using a greedy algorithm.

#pragma GCC optimize("O3", "unroll-loops") // Compiler optimization flags for
                                           // speed and loop unrolling

#include <iosfwd>   // Forward declarations for I/O stream objects
#include <iostream> // I/O stream objects
#include <vector>   // Vector container

// Solution class encapsulates the method to solve the problem
class Solution {
public:
  // Method to calculate the minimum number of rescue boats required
  // Parameters:
  // - people: a vector of integers representing the weights of the people to be
  // rescued
  // - limit: an integer representing the maximum weight that a single boat can
  // carry Returns: an integer representing the minimum number of boats required
  auto numRescueBoats(std::vector<int> &people, int limit) -> int {
    unsigned freq[30001] = {
        0}; // Frequency array to count the occurrence of each weight
    int maxW = 0,
        minW = 30001; // Variables to track the maximum and minimum weights

    // Loop to populate the frequency array and find the max and min weights
    for (int x : people) {
      freq[x]++;
      maxW = std::max(maxW, x);
      minW = std::min(minW, x);
    }

    // Loop to sort the people vector in non-decreasing order of their weights
    for (int i = minW, j = 0; i <= maxW; i++) {
      int f = freq[i];
      fill_n(people.begin() + j, f, i);
      j += f;
    }

    int x = 0; // Variable to count the number of boats required

    // Loop to pair the heaviest and lightest person that can fit in a single
    // boat
    for (int l = 0, r = people.size() - 1; l <= r; r--) {
      x++;
      if (people[l] + people[r] <= limit)
        l++;
    }

    return x; // Return the minimum number of boats required
  }
};

// Initialization block to speed up cin and cout
auto init = []() {
  std::ios::sync_with_stdio(0); // Untie cin from cout
  std::cin.tie(0);              // Untie cin from cout
  std::cout.tie(0);             // Untie cout from cin
  return 'c'; // Return a dummy value to ensure the block is executed
}();
