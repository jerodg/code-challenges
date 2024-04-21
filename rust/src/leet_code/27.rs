impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut i = 0;
        let mut j = nums.len();
        while i < j {
            if nums[i] == val {
                nums[i] = nums[j - 1];
                j -= 1;
            } else {
                i += 1;
            }
        }
        i as i32
    }
}
