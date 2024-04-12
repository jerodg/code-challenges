/**
 * Function to calculate the total amount of trapped rainwater.
 * This function uses the two-pointer technique to find the trapped rainwater.
 *
 * @param height An array of non-negative integers representing the height of
 * each bar.
 * @param heightSize The size of the height array.
 * @return The total amount of rainwater that can be trapped.
 */
int trap(int *height, int heightSize) {
  // Initialize the variables
  int trap = 0, low, high, curr;
  low = 0;
  high = heightSize - 1;

  // Loop until low pointer is less than high pointer
  while (low < high) {
    // If the height at low pointer is less than or equal to the height at high
    // pointer
    if (height[low] <= height[high]) {
      curr = low;
      // Loop until the height at low pointer is less than the height at curr
      // pointer
      while (height[++low] < height[curr]) {
        // Add the difference of height at curr pointer and height at low
        // pointer to trap
        trap += height[curr] - height[low];
      }
    } else {
      curr = high;
      // Loop until the height at high pointer is less than the height at curr
      // pointer
      while (height[--high] < height[curr]) {
        // Add the difference of height at curr pointer and height at high
        // pointer to trap
        trap += height[curr] - height[high];
      }
    }
  }
  // Return the total trapped rainwater
  return trap;
}
