class Solution {
  bool isIsomorphic(String s, String t) {
    if (s.length != t.length) {
      return false;
    }

    Map<String, String> map = {};
    Set<String> set = {};

    for (int i = 0; i < s.length; i++) {
      String key = s[i];
      String value = t[i];

      if (map.containsKey(key)) {
        if (map[key] != value) {
          return false;
        }
      } else {
        if (set.contains(value)) {
          return false;
        }

        map[key] = value;
        set.add(value);
      }
    }

    return true;
  }
}
