object Solution {
  def maxDepth(s: String): Int = {
    var max = 0
    var count = 0
    for (c <- s) {
      if (c == '(') {
        count += 1
        max = max max count
      } else if (c == ')') {
        count -= 1
      }
    }
    max
  }
}
