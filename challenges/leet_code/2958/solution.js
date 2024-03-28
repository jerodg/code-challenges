/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
let maxSubarrayLength = function(nums, k) {
     let left = 0;
    let counter = {};
    let max_length = 0;
    for (let right = 0; right < nums.length; right++) {
        let num = nums[right];
        counter[num] = (counter[num] || 0) + 1;
        while (counter[num] > k) {
            counter[nums[left]] -= 1;
            if (counter[nums[left]] === 0) {
                delete counter[nums[left]];
            }
            left += 1;
        }
        max_length = Math.max(max_length, right - left + 1);
    }
    return max_length;
};
