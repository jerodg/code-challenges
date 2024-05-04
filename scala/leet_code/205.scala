/** This module checks if two given strings are isomorphic.
  * Two strings are isomorphic if the characters in one string can be replaced to get the other string.
  * All occurrences of a character must be replaced with another character while preserving the order of characters.
  * No two characters may map to the same character, but a character may map to itself.
  * The function `isIsomorphic` is the main function in this module.
  */
object Solution {

  /** Function to check if two given strings are isomorphic.
    *
    * @param s a String representing the first input string to be checked.
    * @param t a String representing the second input string to be checked.
    * @return a Boolean value indicating whether the two input strings are isomorphic. Returns true if the strings are isomorphic, false otherwise.
    */
  def isIsomorphic(s: String, t: String): Boolean = {
    // Initialize a mutable map to keep track of the character mappings
    val map = scala.collection.mutable.Map[Char, Char]()
    // Initialize a mutable set to keep track of the characters that have already been mapped
    val set = scala.collection.mutable.Set[Char]()

    // Use the `exists` method to check if there exists an index in the strings where the isomorphism condition is violated
    !(0 until s.length).exists { i =>
      // If the character in `s` at the current index has already been mapped
      if (map.contains(s(i))) {
        // Check if the mapped character is not equal to the character in `t` at the current index
        map(s(i)) != t(i)
      } else {
        // If the character in `t` at the current index has already been mapped
        if (set.contains(t(i))) {
          // The isomorphism condition is violated
          true
        } else {
          // Add the character mapping to the map and the character in `t` at the current index to the set
          map(s(i)) = t(i)
          set += t(i)
          // The isomorphism condition is not violated
          false
        }
      }
    }
  }
}
