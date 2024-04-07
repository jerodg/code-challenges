class Solution {
  public static boolean checkValidString(final String s) {
    int low = 0, high = 0;
    for (char c : s.toCharArray()) {
      if (c == '(') {
        low++;
        high++;
      } else if ((int) c == ')') {
        low--;
        high--;
      } else {
        low--;
        high++;
      }
      if (high < 0) {
        return false;
      }
      low = Math.max(low, 0);
    }
    return low == 0;
  }
}
