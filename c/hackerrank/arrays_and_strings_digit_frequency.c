#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  char s[1000];
  int i, freq[10] = {0};
  scanf("%s", s);
  for (i = 0; i < strlen(s); i++) {
    if (s[i] >= '0' && s[i] <= '9') {
      freq[s[i] - '0']++;
    }
  }
  for (i = 0; i < 10; i++) {
    printf("%d ", freq[i]);
  }
  printf("\n");

  return 0;
}
