/// <summary>
/// This module contains the Solution class which provides a method to find the length of the longest ideal string.
/// </summary>
public class Solution {
    /// <summary>
    /// This method calculates the length of the longest ideal string.
    /// An ideal string is defined as a string where the difference between the ASCII values of any two of its characters is not more than 'k'.
    /// </summary>
    /// <param name="s">The input string. It is expected to be a string of lowercase English alphabets.</param>
    /// <param name="k">The maximum allowed difference between the ASCII values of any two characters in an ideal string. It is expected to be an integer.</param>
    /// <returns>The length of the longest ideal string that can be formed from the input string 's'. The return type is an integer.</returns>
    public int LongestIdealString(string s, int k) {
        // 'len' is an array to store the length of the longest ideal string ending with each character.
        var len = new int[26];
        for (var i = 0; i < s.Length; i++) {
            // 'next' is the length of the longest ideal string ending with the current character.
            var next = 0;
            // For each character in the range [s[i] - k, s[i] + k], update 'next' to be the maximum length of the ideal string ending with that character plus one.
            for (var j = Math.Max(0, s[i] - 'a' - k); j <= Math.Min(25, s[i] - 'a' + k); j++) {
                next = Math.Max(next, len[j] + 1);
            }
            // Update the length of the longest ideal string ending with the current character.
            len[s[i] - 'a'] = next;
        }
        // Return the maximum length among all characters.
        return len.Max();
    }
}
