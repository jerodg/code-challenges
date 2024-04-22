// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <vector>

class Solution {
public:
  int countStudents(std::vector<int>& students, std::vector<int>& sandwiches) {
    int count[2] = {0, 0};
    for (int i = 0; i < students.size(); i++) {
      count[students[i]]++;
    }
    for (int i = 0; i < sandwiches.size(); i++) {
      if (count[sandwiches[i]] == 0) {
        break;
      }
      count[sandwiches[i]]--;
    }
    return count[0] + count[1];
  }
};
