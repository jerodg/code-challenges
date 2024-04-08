object Solution {
  def countStudents(students: Array[Int], sandwiches: Array[Int]): Int = {
    val queue = students.toBuffer
    val stack = sandwiches.toBuffer
    var i = 0
    while (i < queue.length && queue.nonEmpty) {
      if (queue.head == stack.head) {
        queue.remove(0)
        stack.remove(0)
        i = 0
      } else {
        queue.append(queue.remove(0))
        i += 1
      }
    }
    queue.length
  }
}