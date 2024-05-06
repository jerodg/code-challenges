/**
 * @file 950.c
 * @brief This file contains the solution for LeetCode problem 950, "Reveal Cards In Increasing Order".
 *
 * The solution involves sorting the deck of cards in increasing order and then rearranging them according to the problem's rules.
 * The rearrangement is done using a doubly linked list, where we continuously place the top card at the bottom and reveal the new top card.
 *
 * The main function is `deckRevealedIncreasing`, which takes the original deck and its size as input, and returns the rearranged deck.
 */

#include <stdlib.h>

/**
 * @struct list
 * @brief A node in the doubly linked list.
 *
 * Each node contains a value (the card number), and pointers to the next and previous nodes in the list.
 */
struct list {
    int value;
    struct list *nextNode;
    struct list *previousNode;
};

typedef struct list List;

// Function prototypes
void quick_sort(int *, int, int);

void pushFront(List **, List **, int);

void popEnd(List **, List **);

int *listNodeToArray(const List *, int);

/**
 * @brief Rearranges a deck of cards in increasing order according to the problem's rules.
 *
 * @param deck The original deck of cards.
 * @param deckSize The size of the deck.
 * @param returnSize A pointer to an integer where the size of the new deck will be stored.
 * @return The rearranged deck.
 */
int *deckRevealedIncreasing(int *deck, const int deckSize, int *returnSize) {
    List *deckList = NULL, *tail = NULL;

    quick_sort(deck, 0, deckSize - 1);
    pushFront(&deckList, &tail, deck[deckSize - 1]);

    for (int i = deckSize - 2; i >= 0; i--) {
        pushFront(&deckList, &tail, tail->value);
        popEnd(&deckList, &tail);
        pushFront(&deckList, &tail, deck[i]);
    }

    *returnSize = deckSize;
    int *newDeck = listNodeToArray(deckList, *returnSize);

    return newDeck;
}

/**
 * @brief Sorts an array in increasing order using the QuickSort algorithm.
 *
 * @param array The array to be sorted.
 * @param low The starting index of the portion of the array to be sorted.
 * @param high The ending index of the portion of the array to be sorted.
 */
void quick_sort(int array[], const int low, const int high) {
    int partition(int [], int, int);

    if (low < high) {
        int pi = partition(array, low, high);

        quick_sort(array, low, pi - 1);
        quick_sort(array, pi + 1, high);
    }
}

/**
 * @brief Partitions an array for the QuickSort algorithm.
 *
 * @param array The array to be partitioned.
 * @param low The starting index of the portion of the array to be partitioned.
 * @param high The ending index of the portion of the array to be partitioned.
 * @return The index of the pivot element after partitioning.
 */
int partition(int array[], const int low, const int high) {
    void swap(int *, int *);
    int pivot = array[high];
    int i = (low - 1);

    for (int j = low; j < high; j++) {
        if (array[j] <= pivot) {
            i++;
            swap(&array[i], &array[j]);
        }
    }

    swap(&array[i + 1], &array[high]);

    return (i + 1);
}

/**
 * @brief Swaps the values of two integers.
 *
 * @param a Pointer to the first integer.
 * @param b Pointer to the second integer.
 */
void swap(int *a, int *b) {
    const int t = *a;
    *a = *b;
    *b = t;
}

/**
 * @brief Inserts a new node at the front of a doubly linked list.
 *
 * @param headNode Pointer to the head of the list.
 * @param tailNode Pointer to the tail of the list.
 * @param data The value to be inserted.
 */
void pushFront(List **headNode, List **tailNode, const int data) {
    List *newNode = (List *) malloc(sizeof(List));

    if (newNode != NULL) {
        newNode->value = data;
        newNode->nextNode = NULL;
        newNode->previousNode = NULL;

        if (*headNode == NULL) {
            *tailNode = newNode;
        } else {
            (*headNode)->previousNode = newNode;
            newNode->nextNode = *headNode;
        }

        *headNode = newNode;
    }
}

/**
 * @brief Removes the last node of a doubly linked list.
 *
 * @param headNode Pointer to the head of the list.
 * @param tailNode Pointer to the tail of the list.
 */
void popEnd(List **headNode, List **tailNode) {
    if (*tailNode != NULL) {
        List *temp = *tailNode;
        *tailNode = (*tailNode)->previousNode;
        free(temp);
    }
}

/**
 * @brief Converts a doubly linked list to an array.
 *
 * @param headNode The head of the list.
 * @param size The size of the list.
 * @return The array representation of the list.
 */
int *listNodeToArray(const List *headNode, const int size) {
    int i = 0;

    int *array = (int *) malloc(sizeof(int) * size);

    if (array == NULL) return NULL;

    while (headNode != NULL && i <= size - 1) {
        array[i] = headNode->value;
        headNode = headNode->nextNode;
        i++;
    }

    return array;
}
