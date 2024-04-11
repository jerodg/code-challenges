class Solution {
  public boolean isIsomorphic(final String s, final String t) {
    if (s.length() != t.length()) return false;
    final HashMap<Character, Character> map = new HashMap<>();
    final HashSet<Character> set = new HashSet<>();
    for (int i = 0; i < s.length(); i++) {
      final char c1 = s.charAt(i);
      final char c2 = t.charAt(i);
      if (map.containsKey(c1)) {
        if (map.get(c1) != c2) return false;
      } else {
        if (set.contains(c2)) return false;
        map.put(c1, c2);
        set.add(c2);
      }
    }
    return true;
  }
}
