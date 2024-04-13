/// Counts the occurrences of a digit in the square of numbers from 0 to [n].
///
/// This function takes two integers as arguments, [n] and [d]. It generates a list of squares from 0 to [n], converts each square to a string, splits the string into individual digits, and counts the occurrences of the digit [d].
///
/// Example:
/// ```dart
/// var result = nbDig(10, 1);
/// print(result);  // Outputs: 4
/// ```
///
/// [n]: The upper limit of the range of numbers to square.
/// [d]: The digit to count.
/// Returns the count of the digit [d] in the squares of numbers from 0 to [n].
int nbDig(int n, int d) {
  // Generating a list of squares from 0 to n.
  // Converting each square to a string and splitting the string into individual digits.
  // Counting the occurrences of the digit d.
  return List.generate(n + 1, (i) => i * i)
      .map((e) => e.toString().split(''))
      .expand((e) => e)
      .where((e) => e == d.toString())
      .length;
}
