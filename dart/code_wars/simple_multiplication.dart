/// Performs a simple multiplication operation based on the parity of the input.
///
/// This function takes an integer as an argument and returns the result of a multiplication operation. If the integer is even, it is multiplied by 8. If the integer is odd, it is multiplied by 9.
///
/// Example:
/// ```dart
/// var result = simpleMultiplication(2);
/// print(result);  // Outputs: 16
/// ```
///
/// [n]: The integer to perform the operation on.
/// Returns the result of the multiplication operation.
int simpleMultiplication(int n) {
  // Checking if the integer is even.
  if (n % 2 == 0) {
    // If the integer is even, it is multiplied by 8.
    return n * 8;
  } else {
    // If the integer is odd, it is multiplied by 9.
    return n * 9;
  }
}
