// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <string>

using std::string;

class Solution {
public:
  // Function to remove k digits from the number to make it smallest.
  string removeKdigits(const string &num, int k) {
    string s = ""; // Initialize an empty string to store the result.

    // Iterate over each character in the input number.
    for (char c : num) {
      // While the last character in the string is greater than the current
      // character and k is greater than 0, remove the last character from the
      // string and decrement k.
      while (s.size() && s.back() > c && k) {
        --k;
        s.pop_back();
      }

      // If the string is not empty or the current character is not '0',
      // add the current character to the end of the string.
      if (s.size() || c != '0') {
        s.push_back(c);
      }
    }

    // If k is still greater than 0, remove the last character from the string
    // until k is 0.
    while (s.size() && k--) {
      s.pop_back();
    }

    // If the string is empty, return "0". Otherwise, return the string.
    return s.empty() ? "0" : s;
  }
};
