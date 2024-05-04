/**
 * This module is a solution to the Java Static Initializer Block problem on HackerRank.
 * It reads the width and height of a rectangle from the standard input,
 * checks if the width and height are positive, and writes the area of the rectangle to the standard output.
 * If the width or height is not positive, it writes an exception message to the standard output.
 *
 * @author jerodg
 */

import java.util.Scanner;

/**
 * This class contains the main method for the program.
 * It reads the width and height of a rectangle from the standard input,
 * checks if the width and height are positive, and writes the area of the rectangle to the standard output.
 * If the width or height is not positive, it writes an exception message to the standard output.
 */
public class Solution {

    /**
     * The main method for the program.
     * It reads the width and height of a rectangle from the standard input,
     * checks if the width and height are positive, and writes the area of the rectangle to the standard output.
     * If the width or height is not positive, it writes an exception message to the standard output.
     *
     * @param args the command-line arguments for the program
     */
    public static void main(final String[] args) {
        // Initialize the Scanner
        final Scanner in = new Scanner(System.in, java.nio.charset.StandardCharsets.UTF_8);

        // Read the width and height of the rectangle
        final int width = in.nextInt();
        final int height = in.nextInt();

        // Check if the width and height are positive
        if (0 >= width || 0 >= height) {
            // Write an exception message to the standard output
            System.out.println("java.lang.Exception: Breadth and height must be positive");
        } else {
            // Write the area of the rectangle to the standard output
            System.out.println(width * height);
        }

        // Close the Scanner
        in.close();
    }
}
