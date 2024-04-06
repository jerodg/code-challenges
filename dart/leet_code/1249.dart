class Solution {
  String minRemoveToMakeValid(String s) {
    List<int> stack = [];
    List<int> remove = [];
    for (int i = 0; i < s.length; i++) {
      if (s[i] == '(') {
        stack.add(i);
      } else if (s[i] == ')') {
        if (stack.isEmpty) {
          remove.add(i);
        } else {
          stack.removeLast();
        }
      }
    }
    stack.addAll(remove);
    stack.sort();
    String result = '';
    for (int i = 0; i < s.length; i++) {
      if (stack.isNotEmpty && stack.first == i) {
        stack.removeAt(0);
      } else {
        result += s[i];
      }
    }
    return result;
  }
}
