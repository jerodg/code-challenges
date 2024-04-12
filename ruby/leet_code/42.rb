# The `trap` method calculates how much rainwater can be trapped between the bars,
# represented by the array `height`.
#
# @param height [Array<Integer>] an array where each element represents the height of a bar
# @return [Integer] the total amount of rainwater that can be trapped
def trap(height)
  # Number of bars
  num_bars = height.length
  return 0 if num_bars < 1

  # Initialize pointers to the leftmost and rightmost bars
  left_index = 0
  right_index = num_bars - 1

  # Initialize the maximum height of the leftmost and rightmost bars
  left_max_height = height[left_index]
  right_max_height = height[right_index]

  # Initialize the result to 0
  total_water = 0

  # Loop until the left pointer is less than the right pointer
  while left_index < right_index
    # If the maximum height of the left bar is less than the right bar
    if left_max_height < right_max_height
      # Move the left pointer to the right
      left_index += 1
      # Update the maximum height of the left bar
      left_max_height = [left_max_height, height[left_index]].max
      # Add the difference between the maximum height and the current height to the result
      total_water += left_max_height - height[left_index]
    else
      # Move the right pointer to the left
      right_index -= 1
      # Update the maximum height of the right bar
      right_max_height = [right_max_height, height[right_index]].max
      # Add the difference between the maximum height and the current height to the result
      total_water += right_max_height - height[right_index]
    end
  end

  # Return the total amount of water that can be trapped
  total_water
end