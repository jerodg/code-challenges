import 'dart:core';

/// Returns the opposite of a given number.
///
/// This function takes a number as an argument and returns its opposite.
/// It uses the unary minus operator (`-`) to negate the number.
///
/// Example:
/// ```dart
/// var result = opposite(3);
/// print(result);  // Outputs: -3
/// ```
///
/// [n]: The number to negate.
/// Returns the opposite of [n].
num opposite(num n) {
  // Using the unary minus operator to negate the number.
  return -n;
}
