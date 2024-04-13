/// Returns the sum of the first [n] odd numbers in a row.
///
/// This function takes an integer [n] as an argument and returns the sum of the first [n] odd numbers in a row. The sum of the first [n] odd numbers in a row can be calculated as [n] cubed.
///
/// Example:
/// ```dart
/// var result = rowSumOddNumbers(3);
/// print(result);  // Outputs: 27
/// ```
///
/// [n]: The number of the first odd numbers in a row to sum.
/// Returns the sum of the first [n] odd numbers in a row.
int rowSumOddNumbers(int n) {
  // Using the mathematical formula for the sum of the first n odd numbers.
  return n * n * n;
}
