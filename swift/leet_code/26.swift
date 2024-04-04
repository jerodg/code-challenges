class Solution {
    func removeDuplicates(_ nums: inout [Int]) -> Int {
        var slow = 0
        for fast in 1..<nums.count {
            if nums[fast] != nums[slow] {
                slow += 1
                nums[slow] = nums[fast]
            }
        }
        return slow + 1
    }
}