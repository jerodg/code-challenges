#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int a, b;
    scanf("%d\n%d", &a, &b);
    // Complete the code.
    char *str[] = {"one", "two", "three", "four", "five",
                   "six", "seven", "eight", "nine"};
    for (int i = a; i <= b; i++) {
        if (i <= 9) {
            printf("%s\n", str[i - 1]);
        } else {
            if (i % 2 == 0) {
                printf("even\n");
            } else {
                printf("odd\n");
            }
        }
    }
    return 0;
}
