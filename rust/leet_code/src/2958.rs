use std::collections::HashMap;

impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut left = 0;
        let mut counter: HashMap<i32, i32> = HashMap::new();
        let mut max_length = 0;
        for right in 0..nums.len() {
            let num = nums[right];
            let count = counter.entry(num).or_insert(0);
            *count += 1;
            while *counter.get(&num).unwrap() > k {
                *counter.get_mut(&nums[left]).unwrap() -= 1;
                if *counter.get(&nums[left]).unwrap() == 0 {
                    counter.remove(&nums[left]);
                }
                left += 1;
            }
            max_length = max_length.max(right - left + 1);
        }
        max_length as i32
    }
}
