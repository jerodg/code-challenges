object Solution {
  def removeElement(nums: Array[Int], `val`: Int): Int = {
    var i = 0
    for (j <- 0 until nums.length) {
      if (nums(j) != `val`) {
        nums(i) = nums(j)
        i += 1
      }
    }
    i
  }
}