/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
function maxSubarrayLength(nums, k) {
    var left = 0;
    var counter = {};
    var max_length = 0;
    for (var right = 0; right < nums.length; right++) {
        var num = nums[right];
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
}
