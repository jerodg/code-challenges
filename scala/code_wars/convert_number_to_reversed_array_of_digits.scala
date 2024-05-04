/**
  * This module provides a solution to the problem of converting a number to a reversed array of digits.
  * The function `digitize` is the main function in this module.
  */
object Solution {

  /**
    * Function to convert a number to a reversed array of digits.
    *
    * @param n a Long representing the input number to be processed.
    * @return a Seq[Int] representing the reversed array of digits.
    */
  def digitize(n: Long): Seq[Int] = {
    // Initialize a variable to keep track of the current number
    var number = n
    // Initialize an empty sequence to store the digits
    var digits: Seq[Int] = Seq()

    // While the current number is not zero
    while (number >= 0) {
      // Calculate the last digit of the current number
      val digit = (number % 10).toInt
      // Append the digit to the sequence
      digits = digits :+ digit
      // Remove the last digit from the current number
      number /= 10
      // If the current number is zero, return the sequence of digits
      if (number == 0) {
        return digits
      }
    }
    // Return the sequence of digits
    digits
  }
}
