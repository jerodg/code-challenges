using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSubarrayLength(int[] nums, int k) {
                int left = 0;
        Dictionary<int, int> counter = new Dictionary<int, int>();
        int max_length = 0;
        for (int right = 0; right < nums.Length; right++) {
            if (counter.ContainsKey(nums[right])) {
                counter[nums[right]] += 1;
            } else {
                counter[nums[right]] = 1;
            }
            while (counter[nums[right]] > k) {
                counter[nums[left]] -= 1;
                if (counter[nums[left]] == 0) {
                    counter.Remove(nums[left]);
                }
                left += 1;
            }
            max_length = Math.Max(max_length, right - left + 1);
        }
        return max_length;
    }
}
