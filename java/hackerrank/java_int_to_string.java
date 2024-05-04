/**
 * This module is a solution to the Java Int to String problem on HackerRank.
 * It reads an integer from the standard input, converts the integer to a string,
 * checks if the conversion is correct, and writes the result to the standard output.
 *
 * @author jerodg
 */

import java.util.Scanner;

/**
 * This class contains the main method for the program.
 * It reads an integer from the standard input, converts the integer to a string,
 * checks if the conversion is correct, and writes the result to the standard output.
 */
public class Solution {

    /**
     * The main method for the program.
     * It reads an integer from the standard input, converts the integer to a string,
     * checks if the conversion is correct, and writes the result to the standard output.
     *
     * @param args the command-line arguments for the program
     */
    public static void main(final String[] args) {
        // Initialize the Scanner
        final Scanner in = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);

        // Read the integer from the standard input
        final int n = in.nextInt();

        // Convert the integer to a string
        final String s = String.valueOf(n);

        // Check if the conversion is correct and print the result to the standard output
        if (n == Integer.parseInt(s)) {
            System.out.println("Good job");
        } else {
            System.out.println("Wrong answer.");
        }

        // Close the Scanner
        in.close();
    }
}
