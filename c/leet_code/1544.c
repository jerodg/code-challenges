#include <math.h>
#include <stdlib.h>
#include <string.h>

char *makeGood(char *s) {
  int len = strlen(s);
  char *stack = (char *)malloc(len * sizeof(char));
  int top = -1;
  for (int i = 0; i < len; i++) {
    if (top == -1) {
      stack[++top] = s[i];
    } else {
      if (abs(stack[top] - s[i]) == 32) {
        top--;
      } else {
        stack[++top] = s[i];
      }
    }
  }

  char *newStack = (char *)realloc(stack, (top + 2) * sizeof(char));
  if (newStack != NULL) {
    stack = newStack;
    stack[++top] = '\0';
  }
  return stack;
}
