public enum Kata {
  ;

  public static int[] digitize(final long n) {
    final String[] str = new StringBuilder(String.valueOf(n)).reverse().toString().split("");
    final int[] result = new int[str.length];
    for (int i = 0; i < str.length; i++) {
      result[i] = Integer.parseInt(str[i]);
    }
    return result;
  }
}
