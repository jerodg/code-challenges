class Solution {
    func maxSubarrayLength(_ nums: [Int], _ k: Int) -> Int {
        var left = 0
        var counter = [Int: Int]()
        var max_length = 0
        for right in 0..<nums.count {
            counter[nums[right], default: 0] += 1
            while counter[nums[right], default: 0] > k {
                counter[nums[left], default: 0] -= 1
                if counter[nums[left], default: 0] == 0 {
                    counter.removeValue(forKey: nums[left])
                }
                left += 1
            }
            max_length = max(max_length, right - left + 1)
        }
        return max_length
    }
}