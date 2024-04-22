/// Dart implementation of the LeetCode problem 1700: Number of Students Unable to Eat Lunch.
///
/// This module contains a class `Solution` with a method `countStudents`.
/// The `countStudents` method takes in two parameters:
/// - `students`: A list of integers representing the students' sandwich preferences.
/// - `sandwiches`: A list of integers representing the types of sandwiches.
///
/// The method returns an integer representing the number of students who cannot eat lunch.
/// The students are standing in a queue. Each student either prefers the type 0 sandwich or type 1 sandwich.
/// The sandwiches are stacked. Each sandwich is either type 0 or type 1. The students will eat in the following order:
/// - The student at the front of the queue will leave the queue and will eat the sandwich at the top of the stack only if it is the type that they prefer.
/// - Otherwise, they will leave it and wait at the end of the queue. The student will not eat at all if there is no sandwich of their preferred type.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `students` and `sandwiches` are lists of integers.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.

class Solution {
  /// Counts the number of students who cannot eat lunch.
  ///
  /// This method uses a while loop to simulate the process of the students eating the sandwiches.
  /// It iterates until the queue of students is empty. If the student at the front of the queue prefers the sandwich at the top of the stack, the student eats the sandwich and leaves the queue.
  /// Otherwise, the student waits at the end of the queue. If all students in the queue do not prefer the sandwich at the top of the stack, the loop breaks.
  /// After the loop, it returns the number of students who cannot eat lunch.
  ///
  /// @param students The students' sandwich preferences.
  /// @param sandwiches The types of sandwiches.
  /// @return The number of students who cannot eat lunch.
  int countStudents(List<int> students, List<int> sandwiches) {
    int count = 0;
    while (students.isNotEmpty) {
      if (students[0] == sandwiches[0]) {
        students.removeAt(0);
        sandwiches.removeAt(0);
        count = 0;
      } else {
        students.add(students[0]);
        students.removeAt(0);
        count++;
      }
      if (count == students.length) {
        break;
      }
    }
    return students.length;
  }
}
