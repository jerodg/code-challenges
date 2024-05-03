/// <summary>
/// This module contains the Solution class which provides a method to calculate the number of wonderful substrings in a given word.
/// A wonderful string is a string where at most one letter appears an odd number of times.
/// </summary>
public class Solution {
    /// <summary>
    /// Calculates the number of wonderful substrings in a given word.
    /// </summary>
    /// <param name="word">A string representing the word.</param>
    /// <returns>
    /// The number of wonderful substrings in the word.
    /// </returns>
    public long WonderfulSubstrings(string word) {
        // Initialize an array to store the counts of running parity
        int[] runningParityCounts = new int[1024];
        // Initialize the running parity
        int runningParity = 0;
        // Increment the count of the running parity
        runningParityCounts[runningParity]++;

        // Iterate over the characters in the word
        for (int i = 0; i < word.Length; i++) {
            // Update the running parity
            runningParity ^= 1 << (word[i] - 'a');
            // Increment the count of the running parity
            runningParityCounts[runningParity]++;
        }
        // Initialize the total count of wonderful substrings
        long total = 0;

        // Iterate over the possible parities
        for (int parity = 0; parity < 1024; parity++) {
            // Get the count of the current parity
            long count = runningParityCounts[parity];
            // Update the total count of wonderful substrings
            total += count * (count - 1);
            // Iterate over the possible single bit changes
            for (int i = 0; i < 10; i++) {
                // Update the total count of wonderful substrings
                total += count * runningParityCounts[parity ^ (1 << i)];
            }
        }
        // Return the total count of wonderful substrings divided by 2
        return total / 2;
    }
}
