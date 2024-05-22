/// Dart implementation of the LeetCode problem 1544: Make The String Great.
///
/// This module contains a class `Solution` with a method `makeGood`.
/// The `makeGood` method takes in one parameter:
/// - `s`: A string representing the input string.
///
/// The method returns a string representing the "good" string after making the necessary modifications.
/// A string is "good" if there are no two adjacent characters that are of the same letter but different case.
///
/// Error Handling:
/// - This method assumes that the input parameter is well-formed, i.e., `s` is a string of letters.
/// - If the input parameter is not well-formed, the behavior of the method is undefined.
library;

class Solution {
  /// Makes the input string "good".
  ///
  /// This method uses a stack to keep track of the characters in the string.
  /// It iterates over each character in the input string. If the stack is not empty and the last character in the stack is the same letter but different case as the current character, it removes the last character from the stack.
  /// Otherwise, it adds the current character to the stack.
  /// After the iteration, it joins the characters in the stack to form the "good" string.
  ///
  /// @param s The input string.
  /// @return A string representing the "good" string.
  String makeGood(String s) {
    List<String> stack = [];
    for (int i = 0; i < s.length; i++) {
      if (stack.isNotEmpty && stack.last.toLowerCase() == s[i].toLowerCase() && stack.last != s[i]) {
        stack.removeLast();
      } else {
        stack.add(s[i]);
      }
    }
    return stack.join('');
  }
}
