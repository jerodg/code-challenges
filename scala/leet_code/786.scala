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

import scala.collection.mutable.PriorityQueue

/** This object contains a solution for a problem from LeetCode. The problem is about finding the kth smallest prime
  * fraction from an array of integers.
  */
object Solution {

  /** This function finds the kth smallest prime fraction from an array of integers. It uses a priority queue to keep
    * track of the smallest fractions.
    *
    * @param arr
    *   The array of integers from which to find the prime fractions.
    * @param k
    *   The rank of the prime fraction to find.
    * @return
    *   An array of two integers representing the kth smallest prime fraction.
    */
  def kthSmallestPrimeFraction(arr: Array[Int], k: Int): Array[Int] = {
    // Create a priority queue to store the fractions.
    // The ordering is based on the negative of the first element of the tuple,
    // which is the fraction itself. This way, the queue keeps the smallest fractions at the top.
    val pq = new PriorityQueue[(Double, Int, Int)]()(Ordering.by(-_._1))

    // For each element in the array, calculate the fractions with all the elements that come after it.
    for (i <- 0 until arr.size) {
      (arr
        .drop(i + 1))
        .foreach(cur => {
          // Enqueue each fraction into the priority queue.
          pq.enqueue((arr(i).toDouble / cur, arr(i), cur))
        })
    }

    // Dequeue the top k elements from the queue and keep the last one.
    // This will be the kth smallest fraction.
    val res = (0 until k).map(f => pq.dequeue).last

    // Return the kth smallest fraction as an array of two integers.
    Array(res._2, res._3)
  }
}
