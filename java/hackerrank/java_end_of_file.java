import java.util.Scanner;

public class Solution {

  public static void main(final String[] args) {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    // Declare variables
    final Scanner in = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);
    int i = 1;
    while (in.hasNext()) {
      System.out.println(i + " " + in.nextLine());
      i++;
    }
    in.close();
  }
}
