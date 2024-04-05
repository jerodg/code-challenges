object Solution {
  def makeGood(s: String): String = {
    val stack = new scala.collection.mutable.Stack[Char]
    for (c <- s) {
      if (stack.isEmpty) {
        stack.push(c)
      } else {
        if (stack.top.toLower == c.toLower && stack.top != c) {
          stack.pop
        } else {
          stack.push(c)
        }
      }
    }
    stack.reverse.mkString
  }
}
