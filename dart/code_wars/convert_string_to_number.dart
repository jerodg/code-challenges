/// Converts a string to a number.
///
/// This function takes a string as an argument and returns the number equivalent of the string using Dart's built-in `int.parse` method.
///
/// Example:
/// ```dart
/// var result = stringToNumber("123");
/// print(result);  // Outputs: 123
/// ```
///
/// [str]: The string to convert to a number.
/// Returns the number equivalent of the string [str].
int stringToNumber(String str) {
  // Using Dart's built-in int.parse method to convert the string to a number.
  return int.parse(str);
}
