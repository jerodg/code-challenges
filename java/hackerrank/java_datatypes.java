import java.util.Scanner;

public class Solution {

  public static void main(final String[] args) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    // Declare variables
    final Scanner in = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);
    final int t = in.nextInt();
    for (int i = 0; i < t; i++) {
      try {
        final long x = in.nextLong();
        System.out.println(x + " can be fitted in:");
        if (Byte.MIN_VALUE <= x && Byte.MAX_VALUE >= x) {
          System.out.println("* byte");
        }
        if (Short.MIN_VALUE <= x && Short.MAX_VALUE >= x) {
          System.out.println("* short");
        }
        if (Integer.MIN_VALUE <= x && Integer.MAX_VALUE >= x) {
          System.out.println("* int");
        }
        if (Long.MIN_VALUE <= x && Long.MAX_VALUE >= x) {
          System.out.println("* long");
        }
      } catch (final Exception e) {
        System.out.println(in.next() + " can't be fitted anywhere.");
      }
    }
    in.close();
  }
}
