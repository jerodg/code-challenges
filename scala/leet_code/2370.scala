/** This is the `Solution` object, which contains the main logic for the problem. The problem is about finding the
  * longest ideal string given a string `s` and an integer `k`. An ideal string is defined by the problem statement.
  *
  * @example
  *   val s = "abc" val k = 2 val result = Solution.longestIdealString(s, k) println(result) // prints the length of the
  *   longest ideal string
  */
object Solution {

  /** This function calculates the length of the longest ideal string.
    *
    * @param s
    *   the input string
    * @param k
    *   the integer value used to calculate the ideal string
    * @return
    *   the length of the longest ideal string
    */
  def longestIdealString(s: String, k: Int): Int = {

    /** This is a helper function that calculates the length of the longest ideal string using dynamic programming.
      *
      * @param i
      *   the current index in the string `s`
      * @param szs
      *   a map that stores the character and its corresponding length of the longest ideal string
      * @return
      *   the length of the longest ideal string up to index `i`
      */
    def dp(i: Int, szs: Map[Char, Int]): Int = {

      // `nexLen` is a lazy value that calculates the length of the longest ideal string for the current character
      lazy val nexLen: Int = szs
        .collect { case (c, _) if k >= (s(i) - c).abs => szs.getOrElse(c, 0) }
        .maxOption
        .getOrElse(0) + 1

      // If `i` is less than 0, return the maximum length in `szs`, else recursively call `dp` with `i - 1` and updated `szs`
      if (i < 0) szs.values.max else dp(i - 1, szs + (s(i) -> nexLen))
    }

    // Call the helper function `dp` with `s.length - 1` and an empty map
    dp(s.length - 1, Map())
  }
}
