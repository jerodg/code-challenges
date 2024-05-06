/** This module checks if a given string is valid based on the following rules:
  *   - Each '(' must have a corresponding ')'.
  *   - Each ')' must have a corresponding '('.
  *   - '*' can be treated as a single right parenthesis ')', or a single left parenthesis '(', or an empty string. The
  *     function `checkValidString` is the main function in this module.
  */
object Solution {

  /** Function to check if a given string is valid based on the rules defined above.
    *
    * @param s
    *   a String representing the input string to be checked.
    * @return
    *   a Boolean value indicating whether the input string is valid. Returns true if the string is valid, false
    *   otherwise.
    */
  def checkValidString(s: String): Boolean = {
    // Initialize two counters to keep track of the balance of parentheses
    var low  = 0
    var high = 0

    // Use a breakable loop to iterate over the characters in the string
    breakable {
      for (c <- s.toCharArray) {
        // If the character is '(', increment both counters
        if (c == '(') {
          low += 1
          high += 1
        }
        // If the character is ')', decrement both counters
        else if (c == ')') {
          low -= 1
          high -= 1
        }
        // If the character is '*', it can be treated as '(', ')', or an empty string, so decrement low and increment high
        else {
          low -= 1
          high += 1
        }

        // If high is less than 0 at any point, break the loop as the string is not valid
        if (high < 0) {
          break()
        }

        // Ensure low is never less than 0
        low = Math.max(low, 0)
      }
    }

    // If low is 0 after the loop, the string is valid
    low == 0
  }
}
