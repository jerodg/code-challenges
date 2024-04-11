/**
 * This class provides a solution for removing k digits from a number to get the smallest possible
 * number.
 */
class Solution {

  /**
   * Removes k digits from the input number to get the smallest possible number.
   *
   * @param num The input number as a string.
   * @param k The number of digits to remove.
   * @return The smallest possible number as a string after removing k digits.
   */
  public static String removeKdigits(String num, int k) {
    // Convert the input number to a character array
    final char[] digits = num.toCharArray();

    // If the number of digits to remove equals the length of the number, return "0"
    if (k == num.length()) {
      return "0";
    }

    // Initialize a stack to keep track of the digits
    final char[] stack = new char[digits.length];
    int stackTop = -1;
    int removalCount = k;

    // Iterate over each digit in the input number
    for (final char digit : digits) {
      // While there are still digits to remove and the top of the stack is greater than the current
      // digit
      while (removalCount > 0 && stackTop >= 0 && (int) stack[stackTop] > (int) digit) {
        // Pop the top of the stack and decrement the removal count
        stackTop--;
        removalCount--;
      }
      // Push the current digit onto the stack
      stackTop++;
      stack[stackTop] = digit;
    }

    // Find the index of the first non-zero digit
    int nonZeroStart = 0;
    while ((int) stack[nonZeroStart] == '0' && nonZeroStart < digits.length - k - 1) {
      nonZeroStart++;
    }

    // Return the smallest possible number as a string
    return String.valueOf(stack, nonZeroStart, digits.length - k - nonZeroStart);
  }
}
