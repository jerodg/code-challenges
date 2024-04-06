#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

  int n;
  scanf("%d", &n);
  // Complete the code to calculate the sum of the five digits on n.
  int sum = 0;
  while (n > 0) {
    sum += n % 10;
    n /= 10;
  }
  printf("%d\n", sum);

  return 0;
}
