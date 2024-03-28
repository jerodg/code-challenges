from collections import Counter


def longest_good_subarray(nums, k):
    left = 0
    counter = Counter()
    max_length = 0
    for right, num in enumerate(nums):
        counter[num] += 1
        while counter[num] > k:
            counter[nums[left]] -= 1
            if counter[nums[left]] == 0:
                del counter[nums[left]]
            left += 1
        max_length = max(max_length, right - left + 1)

    return max_length
