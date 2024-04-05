public class Kata {
  public static int[] digitize(long n) {
    String[] str = new StringBuilder(String.valueOf(n)).reverse().toString().split("");
    int[] result = new int[str.length];
    for (int i = 0; i < str.length; i++) {
      result[i] = Integer.parseInt(str[i]);
    }
    return result;
  }
}
