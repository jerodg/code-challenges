import java.util.Scanner;

public class Solution {

  public static void main(final String[] args) {
    final Scanner sc = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);
    System.out.println("================================");
    for (int i = 0; 3 > i; i++) {
      final String s1 = sc.next();
      final int x = sc.nextInt();
      // Complete this line

      System.out.printf("%-15s", s1);
      System.out.printf("%03d", x);

      System.out.println();
    }
    System.out.println("================================");
  }
}
