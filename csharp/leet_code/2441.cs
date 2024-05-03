/// <summary>
/// This module contains the Solution class which provides a method to find the maximum negative integer in an array that also has its positive counterpart.
/// </summary>
public class Solution
{
    /// <summary>
    /// Finds the maximum negative integer in the array that also has its positive counterpart.
    /// </summary>
    /// <param name="nums">An array of integers. Both positive and negative integers are allowed.</param>
    /// <returns>
    /// The maximum negative integer that also has its positive counterpart in the array.
    /// If no such number exists, the method returns -1.
    /// </returns>
    public int FindMaxK(int[] nums)
    {
        // Sort the array in ascending order
        Array.Sort(nums);

        // Iterate over the array
        for (int i = 0; i < nums.Length; i++)
        {
            // For each element, iterate over the array again
            for (int j = 0; j < nums.Length; j++)
            {
                // If the negative of the current element equals the element at the mirrored index from the end of the array
                if (nums[i] * (-1) == nums[nums.Length - 1 - j])
                    // Return the negative of the current element
                    return -1*nums[i];
            }
        }

        // If no matching pair is found, return -1
        return -1;
    }
}
