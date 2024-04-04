class Solution {
  int maxSubarrayLength(List<int> nums, int k) {
    int left = 0;
    Map<int, int> counter = {};
    int max_length = 0;
    for (int right = 0; right < nums.length; right++) {
      counter[nums[right]] = (counter[nums[right]] ?? 0) + 1;
      while (counter[nums[right]]! > k) {
        counter[nums[left]] = counter[nums[left]]! - 1;
        if (counter[nums[left]] == 0) {
          counter.remove(nums[left]);
        }
        left++;
      }
      max_length = max(max_length, right - left + 1);
    }
    return max_length;
  }
}