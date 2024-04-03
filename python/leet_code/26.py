class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize two pointers: i and j
        i = 0

        # Iterate over the array with j
        for j in range(1, len(nums)):
            # If a new unique element is found
            if nums[j] != nums[i]:
                # Increment i
                i += 1
                # Place the unique element at the position indicated by i
                nums[i] = nums[j]

        # Return the number of unique elements
        return i + 1
