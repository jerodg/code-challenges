class Solution {
    fun maxSubarrayLength(nums: IntArray, k: Int): Int {
        var left = 0
        val counter = mutableMapOf<Int, Int>()
        var maxLength = 0
        for (right in nums.indices) {
            counter[nums[right]] = counter.getOrDefault(nums[right], 0) + 1
            while (counter[nums[right]]!! > k) {
                counter[nums[left]] = counter[nums[left]]!! - 1
                if (counter[nums[left]]!! == 0) {
                    counter.remove(nums[left])
                }
                left++
            }
            maxLength = maxOf(maxLength, right - left + 1)
        }
        return maxLength
    }
}