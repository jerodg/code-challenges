/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
function maxSubarrayLength(nums: number[], k: number): number {
    let left: number = 0;
    let counter: { [key: number]: number } = {};
    let max_length: number = 0;
    for (let right: number = 0; right < nums.length; right++) {
        let num: number = nums[right];
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
