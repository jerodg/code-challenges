/**
 * This object represents a solution for comparing version numbers.
 * It provides a method to compare two version numbers represented as strings.
 */
object Solution {

  /**
   * Compares two version numbers.
   *
   * This method splits the version numbers by the dot character, converts each part to an integer,
   * and then compares the corresponding parts from both versions. If a version has fewer parts,
   * the missing parts are considered as zero.
   *
   * @param version1 The first version number as a string. It should be a non-negative integer or a sequence of non-negative integers separated by dots.
   * @param version2 The second version number as a string. It should be a non-negative integer or a sequence of non-negative integers separated by dots.
   * @return An integer indicating the result of the comparison. It returns 0 if both versions are equal, a positive integer if the first version is greater, and a negative integer if the second version is greater.
   */
  def compareVersion(version1: String, version2: String): Int = {
    // Split the version strings by the dot character and convert each part to an integer
    val v1Parts: Array[Int] = version1.split('.').map(_.toInt)
    val v2Parts: Array[Int] = version2.split('.').map(_.toInt)

    // Compare the corresponding parts from both versions
    // If a version has fewer parts, the missing parts are considered as zero
    v1Parts
      .zipAll(v2Parts, 0, 0)
      .find(a => a._1 != a._2)
      .map(a => a._1.compare(a._2))
      .getOrElse(0)
  }
}
