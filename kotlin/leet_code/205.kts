/**
 * This Kotlin module provides a solution for the LeetCode problem 205. Isomorphic Strings.
 * The solution determines if two given strings are isomorphic, meaning the characters in the first string can be replaced to get the second string.
 *
 * @module leet_code/205.ws.kts
 */

/**
 * Solution class provides a method to determine if two strings are isomorphic.
 */
class Solution {

    /**
     * This function determines if two strings are isomorphic.
     *
     * @param s The first string to be compared.
     * @param t The second string to be compared.
     * @return A boolean value indicating whether the two strings are isomorphic. Returns true if they are isomorphic, false otherwise.
     *
     * The function uses a map to store the mapping of characters from the first string to the second string, and a set to store the characters that have been mapped.
     * It iterates over the characters in the first string. If a character has been mapped before, it checks if the mapped character is the same as the corresponding character in the second string.
     * If a character has not been mapped before, it checks if the corresponding character in the second string has been mapped. If it has, the function returns false.
     * If the corresponding character in the second string has not been mapped, the function adds the mapping to the map and adds the character to the set.
     * If all characters in the first string can be mapped to the corresponding characters in the second string, the function returns true.
     *
     * Example usage:
     * val solution = Solution()
     * val s = "egg"
     * val t = "add"
     * val isIsomorphic = solution.isIsomorphic(s, t)
     * // isIsomorphic will be true as 'e' can be replaced by 'a' and 'g' can be replaced by 'd' to get 'add'
     */
    fun isIsomorphic(s: String, t: String): Boolean {
        // Initialize a map to store the mapping of characters from s to t
        val map = mutableMapOf<Char, Char>()
        // Initialize a set to store the characters in t that have been mapped
        val set = mutableSetOf<Char>()
        // Iterate over the characters in s
        for (i in s.indices) {
            // If the character in s has been mapped before
            if (map.containsKey(s[i])) {
                // If the mapped character is not the same as the corresponding character in t, return false
                if (map[s[i]] != t[i]) {
                    return false
                }
            } else {
                // If the corresponding character in t has been mapped, return false
                if (set.contains(t[i])) {
                    return false
                }
                // Add the mapping to the map and the character to the set
                map[s[i]] = t[i]
                set.add(t[i])
            }
        }
        // If all characters in s can be mapped to the corresponding characters in t, return true
        return true
    }
}
