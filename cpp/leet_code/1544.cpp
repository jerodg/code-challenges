// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <stack>
#include <string>

class Solution {
public:
  std::string minRemoveToMakeValid(std::string s) {
    int len = s.length();
    std::stack<int> stack;
    for (int i = 0; i < len; i++) {
      if (s[i] == '(') {
        stack.push(i);
      } else if (s[i] == ')') {
        if (!stack.empty()) {
          stack.pop();
        } else {
          s[i] = '*';
        }
      }
    }
    while (!stack.empty()) {
      s[stack.top()] = '*';
      stack.pop();
    }
    std::string result = "";
    for (int i = 0; i < len; i++) {
      if (s[i] != '*') {
        result.push_back(s[i]);
      }
    }
    return result;
  }
};
