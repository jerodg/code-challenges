import java.util.regex.Pattern;

/**
 * The Kata enum provides a method to convert a number into a reversed array of digits.
 * The conversion is done by first reversing the number as a string, then splitting it into individual digits,
 * and finally parsing each digit back into an integer.
 * This enum does not handle any errors explicitly. It assumes that the input parameter `n` is a valid long number.
 * If it is not, the behavior is undefined.
 *
 * @author jerodg
 */
enum Kata {
    ;

    /**
     * A pattern used to split a string into individual characters.
     * In this case, it is an empty string, which means the string will be split between every character.
     */
    private static final Pattern PATTERN = Pattern.compile("");

    /**
     * Converts a long number into a reversed array of digits.
     *
     * @param n The number to be converted. It is a long number.
     *
     * @return An array of integers representing the digits of the number in reversed order.
     */
    public static int[] digitize(long n) {
        // Convert the number into a string, reverse it, and split it into individual characters
        final String[] str = PATTERN.split(new StringBuilder(String.valueOf(n)).reverse().toString());
        // Initialize the result array with the same length as the string array
        final int[] result = new int[str.length];
        // Parse each character back into an integer and store it in the result array
        for (int i = 0; i < str.length; i++) {
            result[i] = Integer.parseInt(str[i]);
        }
        // Return the result array
        return result;
    }
}
