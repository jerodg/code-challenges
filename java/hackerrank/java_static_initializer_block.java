import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int width = in.nextInt();
        int height = in.nextInt();
        if (width <= 0 || height <= 0) {
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        } else {
            System.out.println(width * height);
        }
        in.close();
    }
}