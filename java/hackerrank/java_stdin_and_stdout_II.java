/**
 * This module is a solution to the Java Stdin and Stdout II problem on HackerRank.
 * It reads an integer, a double, and a string from the standard input,
 * and writes them to the standard output in the specified format.
 *
 * @author jerodg
 */

import java.util.Scanner;

/**
 * This class contains the main method for the program.
 * It reads an integer, a double, and a string from the standard input,
 * and writes them to the standard output in the specified format.
 */
public class Solution {

    /**
     * The main method for the program.
     * It reads an integer, a double, and a string from the standard input,
     * and writes them to the standard output in the specified format.
     *
     * @param args the command-line arguments for the program
     */
    public static void main(final String[] args) {
        // Initialize the Scanner
        final Scanner scan = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);

        // Read the integer from the standard input
        final int i = scan.nextInt();

        // Read the double from the standard input
        final double d = scan.nextDouble();

        // Consume the newline character
        scan.nextLine();

        // Read the string from the standard input
        final String s = scan.nextLine();

        // Close the Scanner
        scan.close();

        // Write the string to the standard output
        System.out.println("String: " + s);

        // Write the double to the standard output
        System.out.println("Double: " + d);

        // Write the integer to the standard output
        System.out.println("Int: " + i);
    }
}
