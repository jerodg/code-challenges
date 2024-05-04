/**
 * @fileoverview This module provides a function to compare two version strings.
 * It is used to determine if one version is greater than, equal to, or less than the other.
 * The version strings are expected to be in the format 'x.y.z' where x, y, and z are integers.
 * The comparison is done from left to right, meaning it first compares the major version (x),
 * then the minor version (y), and finally the patch version (z).
 */

/**
 * Compares two version strings.
 *
 * @param {string} ver1 - The first version string to compare. It should be in the format 'x.y.z'.
 * @param {string} ver2 - The second version string to compare. It should be in the format 'x.y.z'.
 * @returns {number} - Returns 0 if the versions are equal, -1 if ver1 is less than ver2, and 1 if ver1 is greater than
 *     ver2.
 */
const compareVersion = function (ver1, ver2) {
    // Split the version strings into arrays of integers
    const nums1 = ver1.split('.').map(n => parseInt(n));
    const nums2 = ver2.split('.').map(n => parseInt(n));

    // Compare the corresponding elements in the arrays
    while (nums1.length > 0 && nums2.length > 0) {
        const num1 = nums1.shift();
        const num2 = nums2.shift();

        // If the elements are equal, continue to the next pair
        if (num1 === num2) {
            continue;
        }

        // If the element from ver1 is less than the element from ver2, return -1
        if (num1 < num2) {
            return -1;
        } else {
            // If the element from ver1 is greater than the element from ver2, return 1
            return 1;
        }
    }

    // If there are remaining elements in ver1 and they are not zero, return 1
    while (nums1.length > 0) {
        const num = nums1.shift();
        if (num === 0) {
            continue;
        }
        return 1;
    }

    // If there are remaining elements in ver2 and they are not zero, return -1
    while (nums2.length > 0) {
        const num = nums2.shift();
        if (num === 0) {
            continue;
        }
        return -1;
    }

    // If all elements have been compared and are equal, return 0
    return 0;
};
