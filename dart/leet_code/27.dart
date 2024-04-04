class Solution {
  int maxDepth(String s) {
    int max = 0;
    int count = 0;
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        count++;
        max = count > max ? count : max;
      } else if (s[i] == ')') {
        count--;
      }
    }
    return max;
  }
}