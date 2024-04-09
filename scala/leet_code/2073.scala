import scala.collection.mutable.PriorityQueue

object Solution {
  def timeRequiredToBuy(tickets: Array[Int], k: Int): Int = {
    val queue = PriorityQueue(tickets: _*)(Ordering.by(-_))
    var time = 0

    while (queue.nonEmpty) {
      val ticketCount = queue.dequeue()
      val decrement = Math.min(ticketCount, k)
      time += decrement

      if (ticketCount - decrement > 0) {
        queue.enqueue(ticketCount - decrement)
      }
    }
    time
  }
}

// fixme: this exceeds the time limit