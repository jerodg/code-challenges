/// Checks if a given string is a palindrome.
///
/// This function takes a string as an argument, converts it to lowercase, and checks if it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
///
/// Example:
/// ```dart
/// var result = isPalindrome("radar");
/// print(result);  // Outputs: true
/// ```
///
/// [x]: The string to check.
/// Returns `true` if [x] is a palindrome, `false` otherwise.
bool isPalindrome(String x) {
  // Converting the string to lowercase to ignore capitalization.
  x = x.toLowerCase();

  // Checking if the string is a palindrome.
  for (int i = 0; i < x.length ~/ 2; i++) {
    // If the characters at the current and mirrored position are not the same, the string is not a palindrome.
    if (x[i] != x[x.length - i - 1]) {
      return false;
    }
  }
  // If all characters at the current and mirrored position are the same, the string is a palindrome.
  return true;
}
