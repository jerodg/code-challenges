/**
 * @file 881.c
 * @brief This module provides functions to calculate the minimum number of boats required to rescue people.
 * @author JerodG <https://github.com/jerodg>
 * @date 04May24
 */

#define OPTIMIZE_LEVEL "O3,unroll-loops"

#pragma GCC optimize(OPTIMIZE_LEVEL)
#include <stdlib.h>

/**
 * @brief Compares two integers.
 * @param a The first integer to compare.
 * @param b The second integer to compare.
 * @return The difference between the two integers.
 */
int compare(const void* a, const void* b) { return (*(int*)b - *(int*)a); }

/**
 * @brief Sorts an array of integers in descending order.
 * @param array The array to sort.
 * @param size The size of the array.
 */
void sort_integers(int* array, const unsigned int size) { qsort(array, size, sizeof(int), compare); }

/**
 * @brief Calculates the minimum number of boats required to rescue people.
 * @param people An array of integers where each integer represents the weight of a person.
 * @param peopleSize The size of the people array.
 * @param limit The maximum weight that a boat can carry.
 * @return The minimum number of boats required.
 *
 * This function first sorts the people array in descending order. Then, it iterates over the array from both ends,
 * trying to fit the heaviest and lightest person in the same boat. If they can't fit together, the heaviest person
 * takes a boat alone. The process continues until all people have been assigned to a boat.
 */
int numRescueBoats(int* people, const int peopleSize, const int limit) {
    sort_integers(people, peopleSize);

    int num_boats = 0;                 // The number of boats required
    int heavy_person = 0;              // Index of the heaviest person who has not yet been assigned to a boat
    int light_person = peopleSize - 1; // Index of the lightest person who has not yet been assigned to a boat

    while (heavy_person <= light_person) {
        if (people[heavy_person] + people[light_person] <= limit) {
            num_boats++;
            heavy_person++;
            light_person--;
        } else {
            num_boats++;
            heavy_person++;
        }
    }
    return num_boats;
}
