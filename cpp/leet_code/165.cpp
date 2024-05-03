// leet_code/165.cpp
// This module provides a solution for comparing two version numbers.
// The version numbers are represented as strings and the comparison is done
// by comparing each segment of the version numbers.
// This module is optimized for speed and unrolls loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <bits/stdc++.h>

// Solution class provides a method for comparing version numbers.
class Solution {
public:
  // compareVersion method compares two version numbers.
  // It takes two strings as input, each representing a version number.
  // It returns 1 if the first version number is greater than the second,
  // -1 if the second version number is greater than the first, and 0 if they
  // are equal. The method handles errors by returning 0 when the version
  // numbers are equal. This method does not throw any exceptions.
  static int compareVersion(const std::string &a, const std::string &b) {
    const int n = a.length(); // Length of the first version number
    const int m = b.length(); // Length of the second version number
    int i = 0, j = 0; // Indices for iterating through the version numbers

    // Compare each segment of the version numbers
    while (i < n && j < m) {
      long long int p = 0, q = 0; // Variables for storing the current segment
                                  // of the version numbers

      // Parse the current segment of the first version number
      while (i < n && a[i] != '.') {
        p = (p * 10) + a[i] - '0';
        i++;
      }

      // Parse the current segment of the second version number
      while (j < m && b[j] != '.') {
        q = (q * 10) + b[j] - '0';
        j++;
      }

      // Compare the current segments
      if (p > q)
        return 1;
      else if (q > p)
        return -1;

      i++;
      j++;
    }

    // Check if there are remaining segments in the first version number
    while (i < n) {
      long long int p = 0; // Variable for storing the current segment of the
                           // first version number

      // Parse the current segment of the first version number
      while (i < n && a[i] != '.') {
        p = (p * 10) + (a[i] - '0');
        i++;
      }

      // If the current segment is greater than 0, the first version number is
      // greater
      if (p > 0)
        return 1;

      i++;
    }

    // Check if there are remaining segments in the second version number
    while (j < m) {
      long long int p = 0; // Variable for storing the current segment of the
                           // second version number

      // Parse the current segment of the second version number
      while (j < m && b[j] != '.') {
        p = (p * 10) + (b[j] - '0');
        j++;
      }

      // If the current segment is greater than 0, the second version number is
      // greater
      if (p > 0)
        return -1;

      j++;
    }

    // If all segments are equal, the version numbers are equal
    return 0;
  }
};
