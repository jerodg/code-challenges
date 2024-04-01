# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}

# fixme: Not working correctly
def max_subarray_length(nums, k)
  sum = 0
  max_len = 0
  left = 0

  nums.each_with_index do |num, right|
    sum += num
    while sum > k
      sum -= nums[left]
      left += 1
    end
    max_len = [max_len, right - left + 1].max
  end

  max_len
end