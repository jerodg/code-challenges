/// Dart implementation of the LeetCode problem 205: Isomorphic Strings.
///
/// This module contains a class `Solution` with a method `isIsomorphic`.
/// The `isIsomorphic` method takes in two parameters:
/// - `s`: A string representing the first input string.
/// - `t`: A string representing the second input string.
///
/// The method returns a boolean indicating whether the two input strings are isomorphic.
/// Two strings are isomorphic if the characters in `s` can be replaced to get `t`.
///
/// Error Handling:
/// - This method assumes that the input parameters are well-formed, i.e., `s` and `t` are strings.
/// - If the input parameters are not well-formed, the behavior of the method is undefined.

class Solution {
  /// Determines whether two strings are isomorphic.
  ///
  /// This method uses a map to keep track of the mapping from characters in `s` to characters in `t`,
  /// and a set to keep track of the characters in `t` that have already been mapped to.
  ///
  /// @param s The first input string.
  /// @param t The second input string.
  /// @return A boolean indicating whether the two input strings are isomorphic.
  bool isIsomorphic(String s, String t) {
    // If the lengths of the strings are not equal, they cannot be isomorphic.
    if (s.length != t.length) {
      return false;
    }

    // Initialize a map to keep track of the mapping from characters in `s` to characters in `t`.
    Map<String, String> map = {};

    // Initialize a set to keep track of the characters in `t` that have already been mapped to.
    Set<String> set = {};

    // Traverse the strings.
    for (int i = 0; i < s.length; i++) {
      String key = s[i];
      String value = t[i];

      // If the current character in `s` has already been mapped to a character in `t`,
      // check if it is mapped to the current character in `t`.
      if (map.containsKey(key)) {
        if (map[key] != value) {
          return false;
        }
      } else {
        // If the current character in `s` has not been mapped and the current character in `t` has already been mapped to,
        // the strings cannot be isomorphic.
        if (set.contains(value)) {
          return false;
        }

        // Map the current character in `s` to the current character in `t` and add the current character in `t` to the set.
        map[key] = value;
        set.add(value);
      }
    }

    // If all characters in `s` can be replaced to get `t`, the strings are isomorphic.
    return true;
  }
}
