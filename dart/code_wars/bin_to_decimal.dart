/// Converts a binary string to a decimal number.
///
/// This function takes a binary string as an argument and returns the decimal equivalent of the binary number using Dart's built-in `int.parse` method with radix 2.
///
/// Example:
/// ```dart
/// var result = binToDec("1011");
/// print(result);  // Outputs: 11
/// ```
///
/// [bin]: The binary string to convert to a decimal number.
/// Returns the decimal equivalent of the binary string [bin].
int binToDec(String bin) {
  // Using Dart's built-in int.parse method to convert the binary string to a decimal number.
  return int.parse(bin, radix: 2);
}
