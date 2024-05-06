import scala.collection.mutable

object Solution {
  def maxSubarrayLength(nums: Array[Int], k: Int): Int = {
    var left       = 0
    val counter    = mutable.HashMap[Int, Int]()
    var max_length = 0
    for (right <- nums.indices) {
      counter.put(nums(right), counter.getOrElse(nums(right), 0) + 1)
      while (counter(nums(right)) > k) {
        counter.put(nums(left), counter(nums(left)) - 1)
        if (counter(nums(left)) == 0) {
          counter.remove(nums(left))
        }
        left += 1
      }
      max_length = Math.max(max_length, right - left + 1)
    }
    max_length
  }
}
