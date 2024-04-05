class Solution {
  String makeGood(String s) {
    List<String> stack = [];
    for (int i = 0; i < s.length; i++) {
      if (stack.isNotEmpty &&
          stack.last.toLowerCase() == s[i].toLowerCase() &&
          stack.last != s[i]) {
        stack.removeLast();
      } else {
        stack.add(s[i]);
      }
    }
    return stack.join('');
  }
}
