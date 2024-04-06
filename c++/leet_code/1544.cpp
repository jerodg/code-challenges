class Solution {
public:
  string minRemoveToMakeValid(string s) {
    int len = s.length();
    stack<int> stack;
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
    string result = "";
    for (int i = 0; i < len; i++) {
      if (s[i] != '*') {
        result.push_back(s[i]);
      }
    }
    return result;
  }
};
