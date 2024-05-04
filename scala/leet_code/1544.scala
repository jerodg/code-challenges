/** This module provides a solution to the problem of making a string "good" by removing all instances of bad characters.
  * A string is "good" if it doesn't have two adjacent characters that are the same, but one is uppercase and the other is lowercase.
  * The function `makeGood` is the main function in this module.
  */
object Solution {

  /** Function to make a string "good" by removing all instances of bad characters.
    * A string is "good" if it doesn't have two adjacent characters that are the same, but one is uppercase and the other is lowercase.
    *
    * @param s a String representing the input string to be processed.
    * @return a String representing the processed string that is "good".
    */
  def makeGood(s: String): String = {
    // Initialize a mutable stack to keep track of the characters in the string
    val stack = new scala.collection.mutable.Stack[Char]

    // Iterate over the characters in the string
    for (c <- s) {
      // If the stack is empty, push the current character onto the stack
      if (stack.isEmpty) {
        stack.push(c)
      } else {
        // If the top character on the stack is the same as the current character but has a different case
        if (stack.top.toLower == c.toLower && stack.top != c) {
          // Pop the top character from the stack
          stack.pop
        } else {
          // Push the current character onto the stack
          stack.push(c)
        }
      }
    }

    // Reverse the stack and convert it to a string
    stack.reverse.mkString
  }
}
