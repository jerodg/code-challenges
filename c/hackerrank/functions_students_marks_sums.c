#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Complete the following function.

int marks_summation(const int *marks, int number_of_students, char gender) {
  // Write your code here.
  int total = 0;
  if (gender == 'g') {
    for (int i = 0; i < number_of_students; i++) {
      if (i % 2 == 1)
        total += marks[i];
    }

  } else if (gender == 'b') {
    for (int i = 0; i < number_of_students; i++) {
      if (i % 2 == 0)
        total += marks[i];
    }
  }
  return total;
}

int main() {
  int number_of_students;
  char gender;
  int sum;

  scanf("%d", &number_of_students);
  int *marks = (int *)malloc(number_of_students * sizeof(int));

  for (int student = 0; student < number_of_students; student++) {
    scanf("%d", (marks + student));
  }

  scanf(" %c", &gender);
  sum = marks_summation(marks, number_of_students, gender);
  printf("%d", sum);
  free(marks);

  return 0;
