int countStudents(int *students, int studentsSize, int *sandwiches,
                  int sandwichesSize) {
  int count[2] = {0, 0};
  for (int i = 0; i < studentsSize; i++) {
    count[students[i]]++;
  }
  for (int i = 0; i < sandwichesSize; i++) {
    if (count[sandwiches[i]] == 0) {
      break;
    }
    count[sandwiches[i]]--;
  }
  return count[0] + count[1];
}
