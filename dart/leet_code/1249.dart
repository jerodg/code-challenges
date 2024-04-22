/// Dart implementation of the LeetCode problem 1249: Minimum Remove to Make Valid Parentheses.
///
/// This module contains a class `Solution` with a method `minRemoveToMakeValid`.
/// The `minRemoveToMakeValid` method takes in one parameter:
/// - `s`: A string representing the input string of parentheses.
///
/// The method returns a string representing the valid parentheses string after removing the minimum number of parentheses.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `s` is a string of parentheses.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.

class Solution {
  /// Removes the minimum number of parentheses to make the input string valid.
  ///
  /// This method uses a stack to keep track of the indices of the open parentheses.
  /// It iterates over each character in the input string. If the character is an open parenthesis, it adds its index to the stack.
  /// If the character is a close parenthesis and the stack is empty, it adds its index to the remove list.
  /// If the character is a close parenthesis and the stack is not empty, it removes the last index from the stack.
  /// After the iteration, it adds the indices in the stack to the remove list and sorts the list.
  /// Then, it constructs the result string by skipping the characters at the indices in the remove list.
  ///
  /// @param s The input string of parentheses.
  /// @return A string representing the valid parentheses string after removing the minimum number of parentheses.
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
