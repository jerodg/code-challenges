/// <summary>
/// This module contains the Solution class which provides a method to compare two version numbers.
/// </summary>
public class Solution {
    /// <summary>
    /// Compares two version numbers.
    /// </summary>
    /// <param name="version1">A string representing the first version number.</param>
    /// <param name="version2">A string representing the second version number.</param>
    /// <returns>
    /// An integer indicating the comparison result.
    /// Returns -1 if the first version is less than the second, 1 if the first version is greater than the second, and 0 if they are equal.
    /// </returns>
    public int CompareVersion(string version1, string version2) {
        // Split the version numbers into arrays
        var split1 = version1.Split(".");
        var split2 = version2.Split(".");
        int i=0;
        int j=0;

        // Iterate over the arrays while there are elements in either of them
        while (i < split1.Length || j < split2.Length) {
            // Get the current element from each array, or 0 if there are no more elements
            int one = i < split1.Length ? Int32.Parse(split1[i]) : 0;
            int two = j < split2.Length ? Int32.Parse(split2[j]) : 0;
            i++; j++;
            // If the elements are equal, continue to the next iteration
            if (one == two) continue;
            // Return the comparison result
            return one < two ? -1 : 1;
        }
        // If all elements have been compared and are equal, return 0
        return 0;
    }
}
