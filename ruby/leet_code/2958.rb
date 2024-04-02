# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_subarray_length(nums, k)
  sum = 0
  max_length = 0
  hash = { 0 => -1 }
  nums.each_with_index do |num, index|
    sum += num
    if hash[sum - k]
      max_length = [max_length, index - hash[sum - k]].max
    else
      hash[sum] = index
    end
  end
  max_length = nums.size if (sum <= k)
  max_length
end