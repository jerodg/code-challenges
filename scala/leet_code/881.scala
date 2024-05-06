/** This module provides a solution to the problem of determining the minimum number of rescue boats required to save
  * people. Each person has a weight, and each boat can carry a maximum weight. The goal is to minimize the number of
  * boats used.
  */

object Solution {

  /** Function to calculate the minimum number of rescue boats required.
    *
    * @param people
    *   an array of integers representing the weights of the people.
    * @param limit
    *   an integer representing the maximum weight a boat can carry.
    * @return
    *   the minimum number of boats required to save all people.
    */
  def numRescueBoats(people: Array[Int], limit: Int): Int = {

    /** Recursive function to calculate the number of boats required.
      *
      * @param max
      *   an integer representing the index of the heaviest person not yet assigned to a boat.
      * @param min
      *   an integer representing the index of the lightest person not yet assigned to a boat.
      * @param boats
      *   an integer representing the number of boats used so far.
      * @return
      *   the number of boats required to save all people.
      */
    @annotation.tailrec
    def plusOneBoat(max: Int, min: Int, boats: Int): Int =
      if (min < max) boats
      else if (people(max) + people(min) <= limit)
        plusOneBoat(max + 1, min - 1, boats + 1)
      else plusOneBoat(max + 1, min, boats + 1)

    people.sortInPlace()(Ordering.Int.reverse)
    plusOneBoat(0, people.length - 1, 0)
  }
}
