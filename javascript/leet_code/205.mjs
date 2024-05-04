/**
 * Function to determine if two strings are isomorphic.
 * Two strings are isomorphic if the characters in one string can be replaced to get the other string.
 *
 * @param {string} s - The first string
 * @param {string} t - The second string
 * @returns {boolean} - True if the strings are isomorphic, false otherwise
 */
const isIsomorphic = function (s, t) {
    // Create maps to store the mapping from characters in s to characters in t and vice versa
    const sMap = new Map();
    const tMap = new Map();

    // Iterate over the characters in the strings
    for (let i = 0; i < s.length; i++) {
        // If the current character in s is already mapped to a character in t and it is not the same as the current
        // character in t
        if (sMap.has(s[i]) && sMap.get(s[i]) !== t[i]) {
            return false;
        }
        // If the current character in t is already mapped to a character in s and it is not the same as the current
        // character in s
        if (tMap.has(t[i]) && tMap.get(t[i]) !== s[i]) {
            return false;
        }
        // Map the current characters in s and t to each other
        sMap.set(s[i], t[i]);
        tMap.set(t[i], s[i]);
    }

    // If all characters in s and t can be mapped to each other, the strings are isomorphic
    return true;
};
