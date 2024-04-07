import scala.util.control.Breaks._

object Solution {
  def checkValidString(s: String): Boolean = {
    var low = 0
    var high = 0
    breakable {
      for (c <- s.toCharArray) {
        if (c == '(') {
          low += 1
          high += 1
        } else if (c == ')') {
          low -= 1
          high -= 1
        } else {
          low -= 1
          high += 1
        }
        if (high < 0) {
          break()
        }
        low = Math.max(low, 0)
      }
    }
    low == 0
  }
}