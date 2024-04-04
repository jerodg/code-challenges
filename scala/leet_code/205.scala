object Solution {
  def isIsomorphic(s: String, t: String): Boolean = {
    val map = scala.collection.mutable.Map[Char, Char]()
    val set = scala.collection.mutable.Set[Char]()
    !(0 until s.length).exists { i =>
      if (map.contains(s(i))) {
        map(s(i)) != t(i)
      } else {
        if (set.contains(t(i))) {
          true
        } else {
          map(s(i)) = t(i)
          set += t(i)
          false
        }
      }
    }
  }
}
