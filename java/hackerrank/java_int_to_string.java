import java.util.Scanner;

public class Solution {

    public static void main(final String[] args) {
        final Scanner in = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);
        final int n = in.nextInt();
        final String s = String.valueOf(n);
        if (n == Integer.parseInt(s)) {
            System.out.println("Good job");
        } else {
            System.out.println("Wrong answer.");
        }
    }
}
