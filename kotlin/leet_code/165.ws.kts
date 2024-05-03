/**
 * This module contains the Solution class which is used to solve the problem of comparing two version numbers.
 *
 * @file leet_code/165.ws.kts
 */
class Solution {
    /**
     * This function compares two version numbers.
     *
     * @param version1 The first version number as a string.
     * @param version2 The second version number as a string.
     * @return Returns 1 if version1 is greater than version2, -1 if version1 is less than version2, and 0 if both versions are equal.
     */
    fun compareVersion(version1: String, version2: String): Int {
        // Create IntStream objects for both version strings
        val stream1 = IntStream(version1)
        val stream2 = IntStream(version2)

        // Initialize result variable to store the comparison result
        var result = 0

        // Continue comparing until the end of either version string is reached
        while (!stream1.isEOF() || !stream2.isEOF()) {
            // Calculate the difference between the current version numbers
            val diff = stream1.readInt() - stream2.readInt()

            // If the difference is positive, version1 is greater
            if (diff > 0) {
                result = 1; break
            }

            // If the difference is negative, version1 is smaller
            if (diff < 0) {
                result = -1; break
            }
        }

        // Return the comparison result
        return result
    }

    /**
     * This class is used to create a stream of integers from a version string.
     *
     * @property string The version string to be converted into an integer stream.
     */
    class IntStream(private val string: String) {

        // Initialize the index to 0
        var i = 0

        /**
         * This function checks if the end of the version string has been reached.
         *
         * @return Returns true if the end of the string has been reached, false otherwise.
         */
        fun isEOF(): Boolean {
            return i >= string.length
        }

        /**
         * This function reads an integer from the version string.
         *
         * @return Returns the next integer in the version string, or 0 if the end of the string has been reached.
         */
        fun readInt(): Int {
            // If the end of the string has been reached, return 0
            if (i == string.length) {
                return 0
            }

            // Initialize the number to 0
            var number = 0

            // Continue reading characters until the end of the string or a '.' is encountered
            while (i < string.length) {
                val c = string[i++]
                if (c == '.') break
                number *= 10
                number += c - '0'
            }
            // Return the number
            return number
        }
    }
}
