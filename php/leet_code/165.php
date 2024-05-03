<?php

/**
 * This module contains the Solution class which provides a method to compare two version numbers.
 * Version numbers consist of one or more revisions separated by a dot '.'. This method compares each revision of the version numbers
 * and returns 1 if version1 > version2, -1 if version1 < version2, and 0 if version1 == version2.
 */

class Solution
{
    /**
     * This method compares two version numbers.
     *
     * @param string $version1 A string representing the first version number.
     * @param string $version2 A string representing the second version number.
     * @return int 1 if version1 > version2, -1 if version1 < version2, and 0 if version1 == version2.
     */
    public function compareVersion(string $version1, string $version2): int
    {
        // Initialize the revisions of the version numbers
        $revision1 = '';
        $revision2 = '';

        $i1 = 0;
        $i2 = 0;
        // Iterate over each character in the version numbers
        while (
            $i1 < strlen($version1) ||
            $i2 < strlen($version2)
        ) {

            $char1 = '';
            // If the end of version1 is reached, set the revision to '0' if it's empty
            if ($i1 == strlen($version1)) {
                if ($revision1 == '') {
                    $revision1 = '0';
                }
            } else {
                $char1 = $version1[$i1];
                // If the character is not a dot, append it to the revision
                if ($char1 != '.') {
                    $revision1 .= $char1;
                    $i1++;
                }
            }

            $char2 = '';
            // If the end of version2 is reached, set the revision to '0' if it's empty
            if ($i2 == strlen($version2)) {
                if ($revision2 == '') {
                    $revision2 = '0';
                }
            } else {
                $char2 = $version2[$i2];
                // If the character is not a dot, append it to the revision
                if ($char2 != '.') {
                    $revision2 .= $char2;
                    $i2++;
                }
            }

            // If a dot or the end of the version numbers is reached, compare the revisions
            if (
                ($char1 == '' || $char1 == '.') &&
                ($char2 == '' || $char2 == '.')
            ) {

                // If the revisions are not equal, break the loop
                if ((int)$revision1 != (int)$revision2) {
                    break;
                }

                // Reset the revisions
                $revision1 = '';
                $revision2 = '';

                // Skip the dots
                if ($char1 == '.') {
                    $i1++;
                }

                if ($char2 == '.') {
                    $i2++;
                }

            }

        }

        // Compare the revisions and return the result
        if ((int)$revision1 < (int)$revision2) {
            return -1;
        }

        if ((int)$revision1 > (int)$revision2) {
            return 1;
        }
        return 0;
    }

}
