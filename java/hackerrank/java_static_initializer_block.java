import java.util.Scanner;

public class Solution {

    public static void main(final String[] args) {
        final Scanner in = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);
        final int width = in.nextInt();
        final int height = in.nextInt();
        if (0 >= width || 0 >= height) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        } else {
            System.out.println(width * height);
        }
        in.close();
    }
}
