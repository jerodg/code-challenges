/// Returns the negative of a given number.
///
/// This function takes a number as an argument and returns its negative. If the number is already negative, it is returned as is. If the number is positive, its negative is returned.
///
/// Example:
/// ```dart
/// var result = makeNegative(5);
/// print(result);  // Outputs: -5
/// ```
///
/// [n]: The number to make negative.
/// Returns the negative of [n].
num makeNegative(num n) {
  // Checking if the number is positive.
  if (n > 0) {
    // If the number is positive, return its negative.
    return -n;
  } else {
    // If the number is already negative, return it as is.
    return n;
  }
}
