/** This module provides a solution to the problem of making a string valid by removing the minimum number of parentheses.
  * A string is valid if and only if:
  * - It is the empty string, or
  * - It can be written as AB (A concatenated with B), where A and B are valid strings, or
  * - It can be written as (A), where A is a valid string.
  * The function `minRemoveToMakeValid` is the main function in this module.
  */
object Solution {

  /** Function to make a string valid by removing the minimum number of parentheses.
    *
    * @param s a String representing the input string to be processed.
    * @return a String representing the processed string that is valid.
    */
  def minRemoveToMakeValid(s: String): String = {
    // Initialize a mutable stack to keep track of the indices of the open parentheses
    val stack = scala.collection.mutable.Stack[Int]()
    // Initialize a mutable set to keep track of the indices of the parentheses to be removed
    val toRemove = scala.collection.mutable.Set[Int]()

    // Iterate over the characters in the string
    for (i <- 0 until s.length) {
      // If the current character is an open parenthesis
      if (s(i) == '(') {
        // Push the index of the open parenthesis onto the stack
        stack.push(i)
      }
      // If the current character is a close parenthesis
      else if (s(i) == ')') {
        // If the stack is empty (there is no matching open parenthesis for the current close parenthesis)
        if (stack.isEmpty) {
          // Add the index of the close parenthesis to the set of indices to be removed
          toRemove.add(i)
        } else {
          // Pop the index of the matching open parenthesis from the stack
          stack.pop()
        }
      }
    }

    // If there are remaining indices in the stack (there are open parentheses without matching close parentheses)
    while (stack.nonEmpty) {
      // Add the indices of the open parentheses to the set of indices to be removed
      toRemove.add(stack.pop())
    }

    // Initialize a mutable string builder to build the processed string
    val sb = new StringBuilder()

    // Iterate over the characters in the string
    for (i <- 0 until s.length) {
      // If the index of the current character is not in the set of indices to be removed
      if (!toRemove.contains(i)) {
        // Append the current character to the string builder
        sb.append(s(i))
      }
    }

    // Return the processed string
    sb.toString()
  }
}
