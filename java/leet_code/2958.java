import java.util.HashMap;

class Solution {
  public int maxSubarrayLength(final int[] nums, final int k) {
    int left = 0;
    final HashMap<Integer, Integer> counter = new HashMap<>();
    int max_length = 0;
    for (int right = 0; right < nums.length; right++) {
      counter.put(nums[right], counter.getOrDefault(nums[right], 0) + 1);
      while (counter.get(nums[right]) > k) {
        counter.put(nums[left], counter.get(nums[left]) - 1);
        if (0 == counter.get(nums[left])) {
          counter.remove(nums[left]);
        }
        left++;
      }
      max_length = Math.max(max_length, right - left + 1);
    }
    return max_length;
  }
}
