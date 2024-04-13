/// Converts a boolean value to a string.
///
/// This function takes a boolean value as an argument and returns its string representation.
/// It uses the `toString` method of the boolean class to convert the boolean value to a string.
///
/// Example:
/// ```dart
/// var result = booleanToString(true);
/// print(result);  // Outputs: true
/// ```
///
/// [b]: The boolean value to convert.
/// Returns the string representation of [b].
String booleanToString(bool b) {
  // Using the toString method of the boolean class to convert the boolean value to a string.
  return b.toString();
}
