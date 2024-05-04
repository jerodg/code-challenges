/**
 * This module is a solution to the Java Output Formatting problem on HackerRank.
 * It reads three pairs of strings and integers from the standard input,
 * formats them according to the problem's requirements, and writes the results to the standard output.
 *
 * @author jerodg
 */

import java.util.Scanner;

/**
 * This class contains the main method for the program.
 * It reads three pairs of strings and integers from the standard input,
 * formats them according to the problem's requirements, and writes the results to the standard output.
 */
public class Solution {

    /**
     * The main method for the program.
     * It reads three pairs of strings and integers from the standard input,
     * formats them according to the problem's requirements, and writes the results to the standard output.
     *
     * @param args the command-line arguments for the program
     */
    public static void main(final String[] args) {
        // Initialize the Scanner
        final Scanner sc = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);

        // Print the header
        System.out.println("================================");

        // Process each pair
        for (int i = 0; 3 > i; i++) {
            // Read the string and the integer
            final String s1 = sc.next();
            final int x = sc.nextInt();

            // Format and print the string and the integer
            System.out.printf("%-15s", s1);
            System.out.printf("%03d", x);

            // Print a newline
            System.out.println();
        }

        // Print the footer
        System.out.println("================================");

        // Close the Scanner
        sc.close();
    }
}
