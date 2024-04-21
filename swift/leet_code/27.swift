class Solution {
    func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
        var slow = 0
        for fast in 0 ..< nums.count {
            if nums[fast] != val {
                nums[slow] = nums[fast]
                slow += 1
            }
        }
        return slow
    }
}
