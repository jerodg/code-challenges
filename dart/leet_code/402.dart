/// Dart implementation of the LeetCode problem 402: Remove K Digits.
///
/// This module contains a class `Solution` with a method `removeKdigits`.
/// The `removeKdigits` method takes in two parameters:
/// - `num`: A string representing the input number.
/// - `k`: An integer representing the number of digits to remove.
///
/// The method returns a string representing the smallest possible number after removing `k` digits from the input number.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `num` is a string and `k` is an integer.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.

class Solution {
  /// Removes `k` digits from the input number to form the smallest possible number.
  ///
  /// This method uses a stack to keep track of the digits. It iterates over each digit in the input number.
  /// If the current digit is less than the top of the stack, it pops the stack until it finds a smaller digit or the stack is empty.
  /// This ensures that the smallest possible number is formed.
  /// If there are still digits to remove after the iteration, it pops the stack until no more digits need to be removed.
  /// Finally, it removes leading zeros from the result and returns it.
  ///
  /// @param num The input number as a string.
  /// @param k The number of digits to remove.
  /// @return The smallest possible number after removing `k` digits.
  String removeKdigits(String num, int k) {
    // If the number of digits to remove is equal to the length of the number, return '0'.
    if (num.length == k) return '0';

    // Initialize an empty stack to keep track of the digits.
    List<int> stack = [];

    // Iterate over each digit in the number.
    for (int i = 0; i < num.length; i++) {
      int digit = int.parse(num[i]);

      // While the stack is not empty, the number of digits to remove is more than 0,
      // and the last digit in the stack is greater than the current digit,
      // remove the last digit from the stack and decrease the number of digits to remove by 1.
      while (stack.isNotEmpty && k > 0 && stack.last > digit) {
        stack.removeLast();
        k--;
      }

      // Add the current digit to the stack.
      stack.add(digit);
    }

    // If there are still digits to remove, remove them from the end of the number.
    while (k > 0) {
      stack.removeLast();
      k--;
    }

    // Convert the stack to a string.
    String result = stack.join();

    // Find the index of the first non-zero digit.
    int nonZeroIndex = 0;
    while (nonZeroIndex < result.length && result[nonZeroIndex] == '0') {
      nonZeroIndex++;
    }

    // If all digits are zero, return '0'. Otherwise, return the number without leading zeros.
    return nonZeroIndex == result.length ? '0' : result.substring(nonZeroIndex);
  }
}
