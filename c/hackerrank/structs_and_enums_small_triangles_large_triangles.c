#include <math.h>
#include <stdio.h>
#include <stdlib.h>

struct triangle {
  int a;
  int b;
  int c;
};

typedef struct triangle triangle;

void sort_by_area(triangle *tr, int n) {
  /**
   * Sort an array a of the length n
   */
  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      double p = (tr[j].a + tr[j].b + tr[j].c) / 2.0;
      double s = sqrt(p * (p - tr[j].a) * (p - tr[j].b) * (p - tr[j].c));
      double p1 = (tr[j + 1].a + tr[j + 1].b + tr[j + 1].c) / 2.0;
      double s1 = sqrt(p1 * (p1 - tr[j + 1].a) * (p1 - tr[j + 1].b) *
                       (p1 - tr[j + 1].c));
      if (s > s1) {
        triangle temp = tr[j];
        tr[j] = tr[j + 1];
        tr[j + 1] = temp;
      }
    }
  }
}

int main() {
  int n;
  scanf("%d", &n);
  triangle *tr = malloc(n * sizeof(triangle));
  for (int i = 0; i < n; i++) {
    scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
  }
  sort_by_area(tr, n);
  for (int i = 0; i < n; i++) {
    printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
  }
  return 0;
}
