#include <malloc.h>

int compare(const void *a, const void *b) {
  return (*(int*)b - *(int*)a);
}

int *deckRevealedIncreasing(int *deck, int deckSize, int *returnSize) {
  int *result = (int *)malloc(deckSize * sizeof(int));
  int *queue = (int *)malloc((deckSize * 2) * sizeof(int)); // Allocate enough spaces
  int front = deckSize, rear = deckSize;

  // Sort the deck in descending order
  qsort(deck, deckSize, sizeof(int), compare);

  // Construct the result
  for (int i = deckSize - 1; i >= 0; i--) {
    if (rear > front) {
      queue[--front] = queue[--rear];
    }
    queue[--front] = deck[i];
  }

  memcpy(result, queue + front, deckSize * sizeof(int));
  *returnSize = deckSize;
  free(queue);
  return result;
}

// fixme: heap buffer overflow
