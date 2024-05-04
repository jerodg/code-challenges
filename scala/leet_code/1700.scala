/**
  * This module provides a solution to the problem of counting the number of students that cannot eat lunch.
  * The students are in a queue and each student either prefers a square sandwich (represented by 0) or a circular sandwich (represented by 1).
  * The sandwiches are in a stack and the sandwich on top of the stack is the one that will be given out next.
  * The students will leave the queue if they get their preferred sandwich, otherwise they will go to the end of the queue.
  * The function `countStudents` is the main function in this module.
  */
object Solution {

  /**
    * Function to count the number of students that cannot eat lunch.
    *
    * @param students an Array[Int] representing the students in the queue. Each student is represented by an integer that indicates their preferred sandwich (0 for square, 1 for circular).
    * @param sandwiches an Array[Int] representing the sandwiches in the stack. Each sandwich is represented by an integer (0 for square, 1 for circular).
    * @return an Int representing the number of students that cannot eat lunch.
    */
  def countStudents(students: Array[Int], sandwiches: Array[Int]): Int = {
    // Initialize a mutable buffer from the students array to represent the queue of students
    val queue = students.toBuffer
    // Initialize a mutable buffer from the sandwiches array to represent the stack of sandwiches
    val stack = sandwiches.toBuffer
    // Initialize a variable to keep track of the number of iterations over the queue
    var i = 0

    // While there are students in the queue and the number of iterations is less than the number of students
    while (i < queue.length && queue.nonEmpty) {
      // If the first student in the queue prefers the sandwich on top of the stack
      if (queue.head == stack.head) {
        // Remove the first student from the queue and the sandwich from the top of the stack
        queue.remove(0)
        stack.remove(0)
        // Reset the number of iterations
        i = 0
      } else {
        // Move the first student to the end of the queue
        queue.append(queue.remove(0))
        // Increment the number of iterations
        i += 1
      }
    }

    // Return the number of students that cannot eat lunch (the number of students remaining in the queue)
    queue.length
  }
}
