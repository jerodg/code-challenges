/**
 * @file leet_code/165.c
 * @brief This module provides functions to compare version numbers.
 *
 * This module contains a function to compare version numbers. It first converts
 * the version numbers into a linked list of integers, then compares the
 * integers in the linked list. The comparison is done from left to right, and
 * the function returns as soon as a difference is found.
 *
 * The module uses a linked list to store the version numbers because the
 * version numbers can be arbitrarily large, and a linked list can handle large
 * numbers without using a lot of memory.
 */

#pragma GCC optimize("O3,unroll-loops")
#include <stdlib.h>
#include <string.h>

/**
 * @brief A node in a linked list of integers.
 *
 * This struct represents a node in a linked list of integers. Each node
 * contains an integer value and a pointer to the next node in the list.
 */
typedef struct node {
  int val;           /**< The integer value of the node. */
  struct node *next; /**< A pointer to the next node in the list. */
} node_t;

/**
 * @brief Converts a version number string into a reversed linked list of
 * integers.
 *
 * This function takes a version number string and converts it into a linked
 * list of integers. The integers are in reverse order, with the least
 * significant integer at the head of the list.
 *
 * @param s The version number string to convert.
 * @param buf A buffer to store the version number string.
 * @return A pointer to the head of the linked list of integers.
 */
node_t *to_int_rev(char *s, char *buf) {
  int start = 0, end = 0;
  const int len = strlen(s);
  bool leftmost = false;
  node_t *hdr = NULL, *tmp, *rev;

  // Loop through the version string, converting each segment to an integer
  while (end < len) {
    // Find the end of the current segment
    for (; s[end] != '.' && s[end] != 0; end++) {
    }

    // Null-terminate the current segment
    s[end] = 0;

    // If this is the first segment, initialize the linked list
    if (leftmost == false) {
      hdr = (node_t *)malloc(sizeof(node_t));
      hdr->next = NULL;
      hdr->val = atoi(&s[start]);
      leftmost = true;
    } else {
      // For subsequent segments, prepend to the linked list
      tmp = (node_t *)malloc(sizeof(node_t));
      tmp->val = atoi(&s[start]);
      tmp->next = hdr;
      hdr = tmp;
    }

    // Move to the next segment
    end++;
    start = end;
  }

  // Reverse the linked list
  for (rev = NULL; hdr;) {
    tmp = hdr;
    hdr = hdr->next;
    tmp->next = rev;
    rev = tmp;
  }

  return rev;
}

/**
 * @brief Compares two version numbers.
 *
 * This function compares two version numbers. It first converts the version
 * numbers into linked lists of integers, then compares the integers in the
 * linked lists. The comparison is done from left to right, and the function
 * returns as soon as a difference is found.
 *
 * @param version1 The first version number to compare.
 * @param version2 The second version number to compare.
 * @return -1 if version1 < version2, 1 if version1 > version2, and 0 if
 * version1 == version2.
 */
int compareVersion(char *version1, char *version2) {
  char v1_str[500], v2_str[500];
  float v1, v2;
  node_t *del;

  // Convert the version strings to linked lists of integers
  node_t *hdr1 = to_int_rev(version1, v1_str);
  node_t *hdr2 = to_int_rev(version2, v2_str);

  node_t *back1 = hdr1;
  node_t *back2 = hdr2;

  // Compare the linked lists
  for (; hdr1 && hdr2; hdr1 = hdr1->next, hdr2 = hdr2->next) {
    if (hdr1->val < hdr2->val) {
      return -1;
    } else if (hdr1->val > hdr2->val) {
      return 1;
    }
  }
  for (; hdr1; hdr1 = hdr1->next) {
    if (hdr1->val > 0) {
      return 1;
    }
  }
  for (; hdr2; hdr2 = hdr2->next) {
    if (hdr2->val > 0) {
      return -1;
    }
  }

  // Free the linked lists
  while (back1) {
    del = back1;
    back1 = back1->next;
    free(del);
  }
  while (back2) {
    del = back2;
    back2 = back2->next;
    free(del);
  }

  return 0;
}
