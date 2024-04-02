# @param {Integer[]} nums
# @return {Integer}
def remove_duplicates(nums)
  return 0 if nums.empty?
  i = 0
  j = 1
  while j < nums.length
    if nums[i] != nums[j]
      i += 1
      nums[i] = nums[j]
    end
    j += 1
  end
  i + 1
end