/**
 * This class provides a solution for comparing version numbers.
 * The version numbers are represented as strings, and the comparison is done by comparing each segment of the version number.
 * The comparison stops as soon as a difference is found.
 * If no difference is found after comparing all segments, the versions are considered equal.
 */
class Solution {

    /**
     * Compares two version numbers.
     *
     * @param version1 the first version number as a string. It is expected to be a non-null string where segments of the version number are separated by '.'.
     * @param version2 the second version number as a string. It is expected to be a non-null string where segments of the version number are separated by '.'.
     *
     * @return an integer indicating the result of the comparison. It returns -1 if version1 is less than version2, 1 if version1 is greater than version2, and 0 if both versions are equal.
     */
    public int compareVersion(String version1, String version2) {
        // Initialize pointers for both versions
        int i = 0, j = 0;

        // Continue comparison as long as there are segments in either version
        while (i < version1.length() || j < version2.length()) {
            // Initialize segment values for this round of comparison
            int num1 = 0, num2 = 0;

            // Construct the segment from version1
            while (i < version1.length() && version1.charAt(i) != '.') {
                num1 = num1 * 10 + (version1.charAt(i) - '0');
                i++;
            }

            // Construct the segment from version2
            while (j < version2.length() && version2.charAt(j) != '.') {
                num2 = num2 * 10 + (version2.charAt(j) - '0');
                j++;
            }

            // Compare the segments
            if (num1 < num2) {
                return -1;
            }
            if (num1 > num2) {
                return 1;
            }

            // Move to the next segment
            i++;
            j++;
        }

        // If all segments are equal, the versions are equal
        return 0;
    }
}
