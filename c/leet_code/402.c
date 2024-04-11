#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to remove k digits from the number to make it smallest
char *removeKdigits(char *num, int k) {
  int i, n = strlen(num), sp = 0;
  // Allocate memory for stack
  char *stack = (char *)malloc((n + 1) * sizeof(char));

  // Iterate over the number
  for (i = 0; i <= n; ++i) {
    // While there are digits in stack and current digit is smaller than top of
    // stack and we can remove more digits
    while (sp > 0 && num[i] < stack[sp - 1] && k > 0) {
      --sp; // remove top digit from stack
      --k;  // decrease the count of removable digits
    }
    // Push current digit to stack
    stack[sp++] = num[i];
  }

  // If there are still digits to remove
  while (k > 0) {
    --sp; // remove top digit from stack
    --k;  // decrease the count of removable digits
  }

  // If stack is empty, return "0"
  if (sp <= 0) {
    free(stack);
    return "0";
  }

  // Null terminate the stack and remove leading zeros
  stack[sp] = '\0';
  i = 0;
  while (stack[i] == '0')
    ++i;

  // If all digits are zero, return "0"
  if (stack[i] == '\0') {
    free(stack);
    return "0";
  }

  // Duplicate the remaining part of stack
  char *result = _strdup(stack + i);
  free(stack);   // free the memory allocated for stack
  return result; // return the result
}

int main() {
  char num[] = "1432219";
  int k = 3;
  char *result = removeKdigits(num, k);
  printf("%s\n", result);
  free(result);
  return 0;
}
