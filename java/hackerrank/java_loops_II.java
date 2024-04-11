import java.util.Scanner;

public class Solution {

  public static void main(final String[] args) {
    final Scanner in = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);
    final int t = in.nextInt();
    for (int i = 0; i < t; i++) {
      final int a = in.nextInt();
      final int b = in.nextInt();
      final int n = in.nextInt();
      int sum = a;
      for (int j = 0; j < n; j++) {
        sum += Math.pow(2, j) * b;
        System.out.print(sum + " ");
      }
      System.out.println();
    }
    in.close();
  }
}
