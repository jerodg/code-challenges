object Solution {

  /** This function removes k digits from the input number string to make the resulting number as small as possible.
    *
    * @param num The input number as a string. It should be a non-negative integer.
    * @param k   The number of digits to remove from the input number. It should be a non-negative integer.
    * @return A string representing the smallest possible number after removing k digits. If the resulting number is empty, return "0".
    * @example removeKdigits("1432219", 3) returns "1219".
    * @example removeKdigits("10200", 1) returns "200".
    * @example removeKdigits("10", 2) returns "0".
    */
  def removeKdigits(num: String, k: Int): String = {
    // Create a mutable stack to hold the digits of the number
    val stack = scala.collection.mutable.Stack[Char]()

    // Initialize the number of digits to remove
    var remove = k

    // Iterate over each character in the number string
    for (c <- num) {
      // While there are still digits to remove and the top of the stack is greater than the current digit, pop the stack
      while (remove > 0 && stack.nonEmpty && stack.top > c) {
        stack.pop()
        remove -= 1
      }
      // Push the current digit onto the stack
      stack.push(c)
    }

    // While there are still digits to remove, pop the stack
    while (remove > 0) {
      stack.pop()
      remove -= 1
    }

    // Create a new StringBuilder to hold the resulting number
    val sb = new StringBuilder()

    // While the stack is not empty, insert the top of the stack at the beginning of the StringBuilder
    while (stack.nonEmpty) {
      sb.insert(0, stack.pop())
    }

    // Convert the StringBuilder to a string and remove leading zeros
    val res = sb.toString().dropWhile(_ == '0')

    // If the resulting string is empty, return "0", otherwise return the resulting string
    if (res.isEmpty()) "0" else res
  }
}
