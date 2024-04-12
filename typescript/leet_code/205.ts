/**
 * @fileoverview This module contains a solution for the "Isomorphic Strings" problem from LeetCode.
 * The problem is solved by using a map to store the mapping from characters in s to characters in t,
 * and a set to store the characters in t that have been mapped to.
 */

/**
 * Function to check if two strings are isomorphic.
 * Two strings s and t are isomorphic if the characters in s can be replaced to get t.
 * @param {string} s - The first string.
 * @param {string} t - The second string.
 * @return {boolean} True if s and t are isomorphic, false otherwise.
 */
function isIsomorphic(s: string, t: string): boolean {
    // Initialize a map to store the mapping from characters in s to characters in t
    let map = new Map<string, string>();
    // Initialize a set to store the characters in t that have been mapped to
    let set = new Set<string>();

    // Iterate over each character in s
    for (let i = 0; i < s.length; i++) {
        // If the current character in s has been mapped
        if (map.has(s[i])) {
            // If the current character in s is not mapped to the current character in t
            if (map.get(s[i]) !== t[i]) return false;
        } else {
            // If the current character in t has been mapped to
            if (set.has(t[i])) return false;
            // Map the current character in s to the current character in t
            map.set(s[i], t[i]);
            // Add the current character in t to the set
            set.add(t[i]);
        }
    }

    // If all characters in s can be replaced to get t, return true
    return true;
}
