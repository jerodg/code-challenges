/**
 * Copyright ©2010-2024 <a href="https://github.com/jerodg/">JerodG</a>
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
 * program. If not, see SSPL.
 */

/**
 * Package leet_code
 *
 * This file contains a function `partition` that partitions a string into all possible palindrome substrings.
 * It uses a helper function `isPalindrome` to check if a substring is a palindrome and a recursive function
 * `backtrack` to generate all possible partitions.
 */

/**
 * Function to partition a string into all possible palindrome substrings.
 *
 * @param {string} s - The string to be partitioned.
 * @returns {string[][]} - An array of arrays, where each inner array is a partition of the string into palindrome
 *     substrings.
 */
const partition = function (s) {
    /**
     * The result array to store all possible partitions.
     * @type {string[][]}
     */
    const result = [];

    /**
     * Helper function to check if a string is a palindrome.
     *
     * @param {string} str - The string to be checked.
     * @returns {boolean} - Returns true if the string is a palindrome, false otherwise.
     */
    const isPalindrome = (str) => {
        let left = 0;
        let right = str.length - 1;

        while (left < right) {
            if (str[left] !== str[right]) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    };

    /**
     * Recursive function to generate all possible partitions of the string.
     *
     * @param {number} start - The starting index for the substring to be checked.
     * @param {string[]} currPartition - The current partition of the string.
     */
    const backtrack = (start, currPartition) => {
        // If the start index is greater than or equal to the length of the string, we have found a valid partition.
        if (start >= s.length) {
            result.push([...currPartition]);
            return;
        }

        // Loop through the string, checking all possible substrings starting from the start index.
        for (let end = start; end < s.length; end++) {
            const substring = s.substring(start, end + 1);
            // If the substring is a palindrome, add it to the current partition and continue the recursion.
            if (isPalindrome(substring)) {
                currPartition.push(substring);
                backtrack(end + 1, currPartition);
                currPartition.pop();
            }
        }
    };

    // Start the recursion with an empty partition.
    backtrack(0, []);
    return result;
};
