/**
 * This module is a solution to the Java End-of-file problem on HackerRank.
 * It reads lines from the standard input until end-of-file is reached,
 * and for each line, it prints the line number and the line itself to the standard output.
 */

import java.util.Scanner;

/**
 * This class contains the main method for the program.
 * It reads lines from the standard input until end-of-file is reached,
 * and for each line, it prints the line number and the line itself to the standard output.
 */
public class Solution {

    /**
     * The main method for the program.
     * It reads lines from the standard input until end-of-file is reached,
     * and for each line, it prints the line number and the line itself to the standard output.
     *
     * @param args the command-line arguments for the program
     */
    public static void main(final String[] args) {
        // Initialize the Scanner
        final Scanner in = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);

        // Initialize the line number
        int i = 1;

        // Read lines from the standard input until end-of-file is reached
        while (in.hasNext()) {
            // Print the line number and the line itself to the standard output
            System.out.println(i + " " + in.nextLine());

            // Increment the line number
            i++;
        }

        // Close the Scanner
        in.close();
    }
}
