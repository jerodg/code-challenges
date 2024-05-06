/** This object represents a solution for finding the number of 'wonderful' substrings in a word. A 'wonderful'
  * substring is defined as a substring where at most one character appears an odd number of times.
  */
object Solution {

  /** Finds the number of 'wonderful' substrings in a word.
    *
    * This method iterates over the word, updating a prefix sum array and a count array. It uses bitwise operations to
    * keep track of the characters that appear an odd number of times in the current substring. It then counts the
    * number of 'wonderful' substrings that end at the current position.
    *
    * @param word
    *   The input word. It should be a string consisting of lowercase English letters.
    * @return
    *   The number of 'wonderful' substrings in the word. It returns a long integer.
    */
  def wonderfulSubstrings(word: String): Long = {
    // The length of the word
    val nLen: Int = word.length

    // The prefix sum array
    var arrSumPref: Array[Int] = Array.ofDim[Int](nLen + 1)

    // Calculate the prefix sum array
    for (nIx <- 0 until nLen) {
      arrSumPref(nIx + 1) = arrSumPref(nIx) ^ (1 << (word(nIx) - 'a'))
    }

    // The count array
    var arrCountLeft: Array[Int] = Array.ofDim[Int](1 << 11)

    // The number of 'wonderful' substrings
    var nAns: Long = 0

    // Count the number of 'wonderful' substrings
    for (nIx <- 0 to nLen) {
      nAns += arrCountLeft(arrSumPref(nIx))
      for (nUnique <- 0 until 10) {
        nAns += arrCountLeft(arrSumPref(nIx) ^ (1 << nUnique))
      }
      arrCountLeft(arrSumPref(nIx)) += 1
      arrSumPref(nIx) = arrCountLeft(arrSumPref(nIx))
    }

    // Return the number of 'wonderful' substrings
    return nAns
  }
}
