/** This module provides a solution to the problem of finding the maximum depth of valid parentheses in a string.
  * The depth of the parentheses in a string is the maximum number of levels of nested parentheses.
  * The function `maxDepth` is the main function in this module.
  */
object Solution {

  /** Function to find the maximum depth of valid parentheses in a string.
    *
    * @param s a String representing the input string to be processed.
    * @return an Int representing the maximum depth of valid parentheses in the string.
    */
  def maxDepth(s: String): Int = {
    // Initialize variables to keep track of the maximum depth and the current depth
    var max = 0
    var count = 0

    // Iterate over the characters in the string
    for (c <- s) {
      // If the current character is an open parenthesis
      if (c == '(') {
        // Increment the current depth
        count += 1
        // Update the maximum depth if the current depth is greater
        max = max max count
      }
      // If the current character is a close parenthesis
      else if (c == ')') {
        // Decrement the current depth
        count -= 1
      }
    }

    // Return the maximum depth
    max
  }
}
