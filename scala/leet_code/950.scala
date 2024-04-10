object Solution {
  def deckRevealedIncreasing(deck: Array[Int]): Array[Int] = {
    def traverse(dk: Seq[Int], acc: Array[Int]): Array[Int] = {
      if (dk.isEmpty) acc
      else traverse(dk.tail, dk.head +: acc.last +: acc.init)
    }
    val sorted = deck.sorted.reverse
    traverse(sorted.tail, Array(sorted.head))
  }
}
