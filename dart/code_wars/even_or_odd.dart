import 'dart:core';

/// Determines whether a given integer is even or odd.
///
/// This function takes an integer as an argument and returns "Even" if the number is even
/// and "Odd" if the number is odd. It uses the modulus operator (`%`) to determine if the
/// number is even or odd. If the remainder of the division of the number by 2 is 0, then
/// the number is even, otherwise it's odd.
///
/// Example:
/// ```dart
/// var result = evenOrOdd(3);
/// print(result);  // Outputs: Odd
/// ```
///
/// [number]: The integer to check.
/// Returns "Even" if [number] is even, "Odd" if [number] is odd.
String evenOrOdd(int number) {
  // Using the modulus operator to check if the number is even or odd.
  return number % 2 == 0 ? "Even" : "Odd";
}
