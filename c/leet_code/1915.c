/**
 * @file leet_code/1915.c
 * @brief This module provides a function to count the number of wonderful
 * substrings.
 *
 * A wonderful string is a string where at most one letter appears an odd number
 * of times. The function `wonderfulSubstrings` takes a string as input, and
 * returns the number of substrings that are wonderful. The function uses
 * bitwise operations to keep track of the frequency of characters.
 */

#include <stdint.h>

/**
 * @brief Counts the number of wonderful substrings in a given string.
 *
 * This function iterates over the string and for each character, it toggles the
 * corresponding bit in a bitmap. It then increments the count of the current
 * bitmap in an array. After the iteration, it calculates the total count of
 * wonderful substrings using the bitmap counts.
 *
 * @param word Pointer to the null-terminated string.
 * @return The number of wonderful substrings in the string, as a 64-bit
 * integer.
 */
long long wonderfulSubstrings(const char *word) {
  char c;              // The current character in the iteration.
  uint16_t bitmap = 0; // The bitmap representing the frequency of characters.
  uint16_t bitmapcount[2048] = {
      0};             // An array to count the occurrences of each bitmap.
  bitmapcount[0] = 1; // Initialize the count of the empty bitmap to 1.

  // Iterate over the string and update the bitmap and its count.
  for (const char *i = word; (c = *(i++));) {
    bitmap ^=
        1 << (c &
              0b1111); // Toggle the bit corresponding to the current character.
    bitmapcount[bitmap]++; // Increment the count of the current bitmap.
  }

  uint64_t count = 0; // The total count of wonderful substrings.
  uint64_t bmcount;   // The count of the current bitmap.

  // Calculate the total count of wonderful substrings.
  for (bitmap = 0; bitmap < 2048; bitmap += 2)
    if ((bmcount = bitmapcount[bitmap])) {
      count +=
          bmcount * (bitmapcount[bitmap ^ 0x400] + bitmapcount[bitmap ^ 0x200] +
                     bitmapcount[bitmap ^ 0x100] + bitmapcount[bitmap ^ 0x080] +
                     bitmapcount[bitmap ^ 0x040] + bitmapcount[bitmap ^ 0x020] +
                     bitmapcount[bitmap ^ 0x010] + bitmapcount[bitmap ^ 0x008] +
                     bitmapcount[bitmap ^ 0x004] + bitmapcount[bitmap ^ 0x002] +
                     bmcount) -
          bmcount;
    }
  return count >> 1; // Return the total count of wonderful substrings.
}
