#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Complete the following function.

void calculate_the_maximum(int n, int k) {
    // Write your code here.
    int maxAnd = 0, maxOr = 0, maxXor = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = i + 1; j <= n; j++) {
            if (((i & j) > maxAnd) && ((i & j) < k)) {
                maxAnd = i & j;
            }
            if (((i | j) > maxOr) && ((i | j) < k)) {
                maxOr = i | j;
            }
            if (((i ^ j) > maxXor) && ((i ^ j) < k)) {
                maxXor = i ^ j;
            }
        }
    }
    printf("%d\n%d\n%d\n", maxAnd, maxOr, maxXor);
}

int main() {
    int n, k;

    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);

    return 0;
}
