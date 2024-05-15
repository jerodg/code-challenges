/**
 * @file leet_code/3075.c
 * @brief This file contains the implementation of functions to solve a problem related to computing the maximum happiness sum.
 *
 * Copyright © 2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
 *
 * This program is free software: you can redistribute it and/or modify it under the terms of the
 * Server Side Public License (SSPL) as published by MongoDB, Inc., either version 1 of the License,
 * or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
 * even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL
 * for more details.
 *
 * The above copyright notice and this permission notice shall be included in all copies or
 * substantial portions of the Software. You should have received a copy of the SSPL along with this
 * program. If not, see <a href="https://www.mongodb.com/licensing/server-side-public-license">SSPL</a>.
 */

#pragma GCC optimize("O3,unroll-loops")

#include <stdlib.h>

/**
 * @brief Sorts an array of unsigned integers using radix sort.
 *
 * Radix sort is a non-comparative integer sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.
 *
 * @param arr The array to be sorted.
 * @param n The size of the array.
 */
void radixsort(unsigned int* arr, int n) {
#define BASESHIFT 8
#define BASE      256
#define BASEMASK  255
    long long mx = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > mx) {
            mx = arr[i];
        }
    }
    for (long long z = 0; (mx >> (z * 8)) > 0; z++) {
        int output[n];
        int count[BASE] = {0};
        for (int i = 0; i < n; i++) {
            count[(arr[i] >> (z * 8)) & BASEMASK]++;
        }
        for (int i = 1; i < BASE; i++) {
            count[i] += count[i - 1];
        }
        for (int i = n - 1; i >= 0; i--) {
            output[count[(arr[i] >> (z * 8)) & BASEMASK] - 1] = arr[i];
            count[(arr[i] >> (z * 8)) & BASEMASK]--;
        }
        for (int i = 0; i < n; i++) {
            arr[i] = output[i];
        }
    }
}

/**
 * @brief Computes the maximum happiness sum of the first k elements in a sorted array.
 *
 * The happiness of an element is defined as the value of the element minus its index. If the happiness is less than or equal to 0, the function returns the current sum.
 *
 * @param happiness The sorted array.
 * @param happinessSize The size of the array.
 * @param k The number of elements to consider.
 * @return long long The maximum happiness sum.
 */
long long maximumHappinessSum(int* happiness, int happinessSize, int k) {
    radixsort(happiness, happinessSize);
    long long c = 0;
    for (int i = 0; i < k; i++) {
        const int hi = happiness[happinessSize - 1 - i] - i;
        if (hi <= 0) {
            return c;
        } else {
            c += hi;
        }
    }
    return c;
}
