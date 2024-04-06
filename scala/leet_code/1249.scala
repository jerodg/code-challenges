object Solution {
  def minRemoveToMakeValid(s: String): String = {
    val stack = scala.collection.mutable.Stack[Int]()
    val toRemove = scala.collection.mutable.Set[Int]()
    for (i <- 0 until s.length) {
      if (s(i) == '(') {
        stack.push(i)
      } else if (s(i) == ')') {
        if (stack.isEmpty) {
          toRemove.add(i)
        } else {
          stack.pop()
        }
      }
    }
    while (stack.nonEmpty) {
      toRemove.add(stack.pop())
    }
    val sb = new StringBuilder()
    for (i <- 0 until s.length) {
      if (!toRemove.contains(i)) {
        sb.append(s(i))
      }
    }
    sb.toString()
  }
}
