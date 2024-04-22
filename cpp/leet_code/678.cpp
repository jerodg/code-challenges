// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <string>

class Solution {
public:
  bool checkValidString(std::pmr::string s) {
    int n = s.size();
    int low = 0, high = 0;
    for (int i = 0; i < n; i++) {
      if (s[i] == '(') {
        low++;
        high++;
      } else if (s[i] == ')') {
        low--;
        high--;
      } else {
        low--;
        high++;
      }
      if (high < 0) {
        return false;
      }
      low = std::max(low, 0);
    }
    return low == 0;
  }
};
