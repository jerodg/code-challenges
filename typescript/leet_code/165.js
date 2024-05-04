/**
 * @file This module contains a function to compare two version numbers.
 * @module leet_code/165
 */
/**
 * Compares two version numbers.
 *
 * This function iterates over the characters of the version numbers, parsing the revisions (numbers separated by
 * dots).
 * It compares each pair of revisions. If a revision is missing in one of the version numbers, it is considered to be
 * zero. The comparison stops as soon as a pair of revisions is found where one is greater than the other, or if both
 * version numbers have been fully parsed.
 *
 * @param {string} version1 - The first version number to compare. It is expected to be a string of digits separated by
 *     dots.
 * @param {string} version2 - The second version number to compare. It is expected to be a string of digits separated
 *     by dots.
 * @returns {number} 1 if version1 is greater than version2, -1 if version1 is less than version2, or 0 if they are
 *     equal.
 *
 * @throws {TypeError} If the inputs are not strings of digits separated by dots.
 */
function compareVersion(version1, version2) {
    if (typeof version1 !== 'string' || !/^\d+(\.\d+)*$/.test(version1) ||
        typeof version2 !== 'string' || !/^\d+(\.\d+)*$/.test(version2)) {
        throw new TypeError('Inputs must be strings of digits separated by dots');
    }
    var i = 0;
    var j = 0;
    while (i < version1.length || j < version2.length) {
        // find first valid digit
        var revision1 = '0';
        var noLeadingZero = false;
        for (var k = i; k < version1.length; k++, i++) {
            if (version1[k] === '.') {
                i++;
                break;
            }
            else {
                if (version1[k] !== '0' || noLeadingZero) {
                    revision1 += version1[k];
                    noLeadingZero = true;
                }
            }
        }
        var revision2 = '0';
        noLeadingZero = false;
        for (var k = j; k < version2.length; k++, j++) {
            if (version2[k] === '.') {
                j++;
                break;
            }
            else {
                if (version2[k] !== '0' || noLeadingZero) {
                    revision2 += version2[k];
                    noLeadingZero = true;
                }
            }
            j = k;
        }
        var n1 = parseInt(revision1);
        var n2 = parseInt(revision2);
        if (n1 > n2) {
            return 1;
        }
        else if (n1 < n2) {
            return -1;
        }
    }
    return 0;
}
