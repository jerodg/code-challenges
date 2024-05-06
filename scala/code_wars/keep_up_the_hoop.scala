/** This function determines the feedback message for a hoop exercise based on the input number.
  *
  * @param n
  *   The input number representing the hoop count. It should be an integer.
  * @return
  *   A string message based on the hoop count. If the count is 10 or more, the function returns "Great, now move on to
  *   tricks". If the count is less than 10, the function returns "Keep at it until you get it".
  */
def hoopCount(n: Int): String = {
  if (n >= 10) {
    "Great, now move on to tricks"
  } else {
    "Keep at it until you get it"
  }
}
