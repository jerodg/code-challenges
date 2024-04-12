/**
 * Calculates how much water can be trapped between the bars in a bar chart.
 * @param {number[]} height - An array of non-negative integers representing the heights of the bars.
 * @return {number} - The total amount of water that can be trapped.
 */
const trap = function (height) {
    // Initialize pointers and variables
    let left = 0, right = height.length - 1, lmax = 0, rmax = 0, water = 0;

    // Loop until the two pointers meet
    while (left < right) {
        // If the bar on the left is shorter or equal to the bar on the right
        if (height[left] <= height[right]) {
            // If the current bar is taller than the tallest bar we've seen from the left
            if (height[left] > lmax) {
                // Update the tallest bar from the left
                lmax = height[left];
            } else {
                // Add the difference between the tallest bar from the left and the current bar to the total
                water += lmax - height[left];
            }
            // Move the left pointer to the right
            left++;
        } else {
            // If the current bar is taller than the tallest bar we've seen from the right
            if (height[right] > rmax) {
                // Update the tallest bar from the right
                rmax = height[right];
            } else {
                // Add the difference between the tallest bar from the right and the current bar to the total
                water += rmax - height[right];
            }
            // Move the right pointer to the left
            right--;
        }
    }
    // Return the total amount of water that can be trapped
    return water;
};
