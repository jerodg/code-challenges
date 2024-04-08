class Solution {
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
