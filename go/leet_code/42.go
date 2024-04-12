package leet_code

// trap calculates the total amount of water that can be trapped between the bars.
// The heights of the bars are given by the `height` array.
// It uses two pointers, `left` and `right`, starting from the ends of the array and moving towards the center.
// `leftWall` and `rightWall` keep track of the highest bar from the left and right, respectively.
// The water trapped at a certain index is the difference between the height of the wall and the height of the bar at that index.
func trap(height []int) int {
	left, right := 0, len(height)-1 // Initialize pointers at both ends of the array.
	leftWall, rightWall := 0, 0     // Initialize the left and right walls with height 0.
	ans := 0                        // Initialize the answer, which is the total amount of trapped water.

	// Move the pointers towards the center.
	for left < right {
		// If the bar at the left pointer is shorter than the bar at the right pointer,
		// update the left wall and add the trapped water at the left index to the answer.
		if height[left] < height[right] {
			leftWall = max(height[left], leftWall)
			ans += leftWall - height[left]
			left++
		} else {
			// If the bar at the right pointer is shorter or equal to the bar at the left pointer,
			// update the right wall and add the trapped water at the right index to the answer.
			rightWall = max(height[right], rightWall)
			ans += rightWall - height[right]
			right--
		}
	}

	// Return the total amount of trapped water.
	return ans
}
