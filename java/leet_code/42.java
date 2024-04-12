/**
 * Solution class for LeetCode problem 42.
 */
class Solution {

  /**
   * Method to calculate the total amount of trapped rainwater.
   *
   * @param height an array representing the height of bars
   * @return the total amount of rainwater that can be trapped
   */
  public static int trap(final int[] height) {
    // Get the length of the height array
    final int n = height.length;

    // If there are no bars, no water can be trapped
    if (n == 0) return 0;

    // Initialize arrays to store the maximum height of bars on the left and right
    final int[] left = new int[n];
    final int[] right = new int[n];

    // The first bar has no bars on its left, so it can't trap any water
    left[0] = height[0];

    // The last bar has no bars on its right, so it can't trap any water
    right[n - 1] = height[n - 1];

    // Fill the left array with the maximum height of bars on the left
    for (int i = 1; i < n; i++) {
      left[i] = Math.max(left[i - 1], height[i]);
    }

    // Fill the right array with the maximum height of bars on the right
    for (int i = n - 2; i >= 0; i--) {
      right[i] = Math.max(right[i + 1], height[i]);
    }

    // Initialize the total amount of trapped water
    int ans = 0;

    // Calculate the total amount of trapped water
    for (int i = 0; i < n; i++) {
      ans += Math.min(left[i], right[i]) - height[i];
    }

    // Return the total amount of trapped water
    return ans;
  }
}