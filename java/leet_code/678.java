enum Solution {
  ;

  public static boolean checkValidString(String s) {
    int low = 0, high = 0;
    for (final char c : s.toCharArray()) {
      if ('(' == c) {
        low++;
        high++;
      } else if (')' == (int) c) {
        low--;
        high--;
      } else {
        low--;
        high++;
      }
      if (0 > high) {
        return false;
      }
      low = Math.max(low, 0);
    }
    return 0 == low;
  }
}
