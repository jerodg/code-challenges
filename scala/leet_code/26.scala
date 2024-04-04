object Solution {
  def removeDuplicates(nums: Array[Int]): Int = {
    if (nums.isEmpty) return 0
    var i = 0
    for (j <- 1 until nums.length) {
      if (nums(j) != nums(i)) {
        i += 1
        nums(i) = nums(j)
      }
    }
    i + 1
  }
}