import java.util.Scanner;

public class Solution {

    public static void main(final String[] args) {
        final Scanner scan = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);
        final int i = scan.nextInt();
        final double d = scan.nextDouble();
        // Consume the newline character
        scan.nextLine();
        final String s = scan.nextLine();
        scan.close();

        System.out.println("String: " + s);
        System.out.println("Double: " + d);
        System.out.println("Int: " + i);
    }
}
