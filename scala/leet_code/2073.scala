/**
  * This module provides a solution to the problem of calculating the time required to buy tickets.
  * Given an array of integers representing the number of tickets available at each ticket window and an integer representing the position of a person in the queue,
  * the function `timeRequiredToBuy` calculates the time required for the person to buy a ticket.
  * The time required to buy a ticket from a window is equal to the number of tickets available at that window.
  * Each person in the queue buys one ticket from the window with the most tickets available.
  * If there is a tie for the window with the most tickets available, the person buys a ticket from the window with the lowest index.
  * The person at the front of the queue is at position 0, the next person is at position 1, and so on.
  * The person in the queue buys a ticket from the window with the most tickets available that is not ahead of them in the queue.
  */
object Solution {

  /**
    * Function to calculate the time required for a person to buy a ticket.
    *
    * @param tickets an Array[Int] representing the number of tickets available at each ticket window.
    * @param k an Int representing the position of the person in the queue.
    * @return an Int representing the time required for the person to buy a ticket.
    */
  def timeRequiredToBuy(tickets: Array[Int], k: Int): Int =
    // Iterate over the indices of the tickets array
    tickets.indices.foldLeft(0)((sum, n) =>
      // Add the minimum of the number of tickets available at the current window and the number of tickets available at the kth window (or one less if the current window is ahead of the kth window in the queue) to the sum
      sum + tickets(n).min(if (n > k) tickets(k) - 1 else tickets(k))
    )
}
