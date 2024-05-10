/** Copyright ©2012-2024 JerodG <https://github.com/jerodg/>
  *
  * This program is free software: you can redistribute it and/or modify it under the terms of the Server Side Public
  * License (SSPL) as published by MongoDB, Inc., either version 1 of the License, or (at your option) any later
  * version.
  *
  * This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
  * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the SSPL for more details.
  *
  * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
  * Software. You should have received a copy of the SSPL along with this program. If not, see
  * <https://www.mongodb.com/licensing/server-side-public-license>.
  */

/** The `Solution` object contains a method to calculate the maximum happiness sum. This is achieved by sorting the
  * happiness array and then adding the maximum values from the sorted array, subtracting the index for each iteration.
  */
object Solution {
  import scala.util.Random

  /** This method calculates the maximum happiness sum.
    *
    * @param happiness
    *   An array of integers representing happiness values.
    * @param k
    *   The number of elements to consider from the sorted happiness array.
    * @return
    *   The maximum possible sum of happiness values, subtracting the index for each iteration.
    */
  def maximumHappinessSum(happiness: Array[Int], k: Int): Long = {
    // Sort the happiness array in ascending order
    val sorted = happiness.sorted

    // Initialize the result to 0
    var res = 0L

    // Initialize the index to 0
    var i = 0

    // Loop over the sorted array from the end, subtracting the index for each iteration
    while (i < k) {
      // Add the maximum value between 0 and the current element minus the index to the result
      res += Math.max(0, sorted(sorted.length - i - 1) - i)
      // Increment the index
      i += 1
    }

    // Return the result
    res
  }
}
