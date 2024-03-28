class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
                int left = 0;
        HashMap<Integer, Integer> counter = new HashMap<>();
        int max_length = 0;
        for (int right = 0; right < nums.length; right++) {
            counter.put(nums[right], counter.getOrDefault(nums[right], 0) + 1);
            while (counter.get(nums[right]) > k) {
                counter.put(nums[left], counter.get(nums[left]) - 1);
                if (counter.get(nums[left]) == 0) {
                    counter.remove(nums[left]);
                }
                left++;
            }
            max_length = Math.max(max_length, right - left + 1);
        }
        return max_length;
    }
}
