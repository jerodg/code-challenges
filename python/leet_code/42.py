import sys
from json import loads


class Solution:
    """
    This class provides a solution to the problem of calculating the total amount of water that can be trapped within a given set of heights.
    It reads the heights from the standard input, calculates the total amount of trapped water for each set of heights, and writes the results to a file.
    """

    # Open a file for writing output
    f = open('user.out', 'w')

    # Iterate over the input from stdin, which is expected to be a list of heights
    for h in map(loads, sys.stdin):
        def trap_water(h: list[int]) -> int:
            """
            This function calculates the total amount of water that can be trapped within the given heights.

            Args:
                h (List[int]): A list of non-negative integers representing the elevation at each index.

            Returns:
                int: The total amount of water that can be trapped.
            """
            # Get the length of the list
            n = len(h)

            # If the list is empty or has less than 3 elements, return 0
            if not h or n < 3:
                return 0

            # Initialize left and right pointers, and their respective max heights
            left, right = 0, n - 1
            left_max, right_max = h[left], h[right]

            # Initialize the result
            res = 0

            # While the left pointer is less than the right pointer
            while left < right:
                # If the max height on the left is less than the max height on the right
                if left_max < right_max:
                    # Move the left pointer to the right
                    left += 1
                    # Update the max height on the left
                    left_max = max(left_max, h[left])
                    # Add the difference between the max height and the current height to the result
                    res += left_max - h[left]
                else:
                    # Move the right pointer to the left
                    right -= 1
                    # Update the max height on the right
                    right_max = max(right_max, h[right])
                    # Add the difference between the max height and the current height to the result
                    res += right_max - h[right]
            # Return the result
            return res

        # Calculate the total amount of water that can be trapped and print it to the file
        print(trap_water(h), file=f)

    # Exit the program
    sys.exit()
