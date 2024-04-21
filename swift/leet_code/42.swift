/**
 A `Solution` class that provides a method to calculate the trapping rain water.

 This class provides a method `trap` which calculates how much rain water can be trapped between the bars, given the heights of the bars. The heights of the bars are represented as an array of integers.

 - Note: The `trap` method uses a two-pointer approach to solve the problem.

 - Complexity: This method runs in O(n) time, where n is the number of bars. It uses O(1) extra space.
 */
class Solution {
    /**
     Calculate the amount of trapped rain water.

     This method calculates and returns the total amount of rain water that can be trapped, given the heights of the bars.

     - Parameter height: An array of integers where each integer represents the height of a bar.
     - Returns: The total amount of trapped rain water.

     - Note: If the height array is empty, this method will return 0.
     */
    func trap(_ height: [Int]) -> Int {
        var leftMax = 0 // Maximum height of the bar from the left up to the current position
        var rightMax = 0 // Maximum height of the bar from the right up to the current position
        var lp = 0 // Left pointer
        var rp = height.count - 1 // Right pointer
        var result = 0 // Resultant trapped water

        // Loop until the two pointers meet
        while lp < rp {
            if height[lp] <= height[rp] {
                if height[lp] >= leftMax {
                    leftMax = height[lp] // Update the left maximum
                } else {
                    result += leftMax - height[lp] // Calculate the trapped water
                }
                lp += 1 // Move the left pointer
            } else {
                if height[rp] >= rightMax {
                    rightMax = height[rp] // Update the right maximum
                } else {
                    result += rightMax - height[rp] // Calculate the trapped water
                }
                rp -= 1 // Move the right pointer
            }
        }
        return result // Return the total trapped water
    }
}
