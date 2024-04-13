/// Repeats a given string a specified number of times.
///
/// This function takes an integer and a string as arguments. It returns a new string that consists of the input string repeated the number of times specified by the integer.
///
/// Example:
/// ```dart
/// var result = repeatString(3, "hello");
/// print(result);  // Outputs: hellohellohello
/// ```
///
/// [n]: The number of times to repeat the string.
/// [s]: The string to repeat.
/// Returns the string [s] repeated [n] times.
String repeatString(int n, String s) {
  // Using Dart's built-in string multiplication operator to repeat the string.
  return s * n;
}
