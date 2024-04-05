class Solution {
public:
  string makeGood(string s) {
    int len = s.length();
    string stack = "";
    for (int i = 0; i < len; i++) {
      if (stack.empty()) {
        stack.push_back(s[i]);
      } else {
        if (abs(stack.back() - s[i]) == 32) {
          stack.pop_back();
        } else {
          stack.push_back(s[i]);
        }
      }
    }
    return stack;
  }
};
