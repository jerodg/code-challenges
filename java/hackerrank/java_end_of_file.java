import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        // Declare variables
        Scanner in = new Scanner(System.in);
        int i = 1;
        while (in.hasNext()) {
            System.out.println(i + " " + in.nextLine());
            i++;
        }
        in.close();

    }
}