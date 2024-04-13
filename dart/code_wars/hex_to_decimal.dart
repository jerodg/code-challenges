import 'dart:core';

/// Converts a hexadecimal string to a decimal integer.
///
/// This function takes a hexadecimal string as an argument and returns its decimal equivalent.
/// It uses the `int.parse` function with radix 16 to convert the hexadecimal string to a decimal integer.
///
/// Example:
/// ```dart
/// var result = hexToDec('A');
/// print(result);  // Outputs: 10
/// ```
///
/// [hexString]: The hexadecimal string to convert.
/// Returns the decimal equivalent of [hexString].
int hexToDec(String hexString) {
  // Using int.parse with radix 16 to convert the hexadecimal string to a decimal integer.
  return int.parse(hexString, radix: 16);
}
