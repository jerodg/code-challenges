#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

  int n;
  scanf("%d", &n);
  // Complete the code to print the pattern.
  int len = n * 2 - 1;
  for (int i = 0; i < len; i++) {
    for (int j = 0; j < len; j++) {
      int min = i < j ? i : j;
      min = min < len - i ? min : len - i - 1;
      min = min < len - j - 1 ? min : len - j - 1;
      printf("%d ", n - min);
    }
    printf("\n");
  }
  return 0;
}
