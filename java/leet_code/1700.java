class Solution {
  public int countStudents(final int[] students, final int[] sandwiches) {
    final int[] count = new int[2];
    for (final int student : students) {
      count[student]++;
    }

    for (final int sandwich : sandwiches) {
      if (0 == count[sandwich]) {
        break;
      }
      count[sandwich]--;
    }

    return count[0] + count[1];
  }
}
