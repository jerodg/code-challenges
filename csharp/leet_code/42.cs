using System;

public class Solution {
    // Function to calculate the amount of trapped rainwater
    public int Trap(int[] height) {
        // Initialize pointers to the start and end of the array
        int left = 0;
        int right = height.Length - 1;

        // Initialize the answer and the maximum height from both ends
        int ans = 0;
        int leftMax = 0;
        int rightMax = 0;

        // Loop until the two pointers meet
        while (left < right)
        {
            // If the height at the left pointer is less than the height at the right pointer
            if (height[left] < height[right]) 
            {
                // If the current height is greater than or equal to the maximum height from the left
                // Update the maximum height from the left
                if (height[left] >= leftMax)
                {
                    leftMax = height[left];
                } 
                // If the current height is less than the maximum height from the left
                // Add the difference to the answer
                else 
                {
                    ans += (leftMax - height[left]);
                }
                // Move the left pointer to the right
                left++;
            } 
            // If the height at the right pointer is less than or equal to the height at the left pointer
            else 
            {
                // If the current height is greater than or equal to the maximum height from the right
                // Update the maximum height from the right
                if (height[right] >= rightMax)
                {
                    rightMax = height[right];
                } 
                // If the current height is less than the maximum height from the right
                // Add the difference to the answer
                else 
                {
                    ans += (rightMax - height[right]);
                }
                // Move the right pointer to the left
                right--;
            }
        }
        // Return the total amount of trapped rainwater
        return ans;
    }
}