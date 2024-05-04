import java.util.Arrays;

/**
 * This class provides a solution for the problem of revealing cards in increasing order.
 * The problem is solved by sorting the deck of cards and then placing them in the result array in a specific order.
 * The order is determined by skipping every other empty spot in the result array until all spots are filled.
 * The process is repeated until all cards are placed in the result array.
 */
public class Solution {
    /**
     * Reveals cards in increasing order.
     *
     * @param deck An array of integers representing the deck of cards. Each integer is a non-negative integer.
     *
     * @return An array of integers representing the order in which the cards are revealed. Each integer is a non-negative integer.
     */
    public static int[] deckRevealedIncreasing(final int[] deck) {
        final int N = deck.length;
        final int[] result = new int[N];
        Arrays.sort(deck);

        return Solution.everyOther(deck, result, 0, false);
    }

    /**
     * Places cards in every other empty spot in the result array.
     *
     * @param deck        An array of integers representing the sorted deck of cards. Each integer is a non-negative integer.
     * @param result      An array of integers representing the current order in which the cards are revealed. Each integer is a non-negative integer.
     * @param indexInDeck The index of the next card to be placed in the result array. It is a non-negative integer.
     * @param skip        A boolean indicating whether the next empty spot in the result array should be skipped.
     *
     * @return An array of integers representing the updated order in which the cards are revealed. Each integer is a non-negative integer.
     */
    private static int[] everyOther(
            final int[] deck, final int[] result, final int indexInDeck, final boolean skip) {
        int inDeck = indexInDeck;
        boolean b = skip;
        int inResult = 0;
        final int N = deck.length;

        if (inDeck == N) {
            return result;
        }

        while (inResult < N) {
            if (0 == result[inResult]) {
                if (!b) {
                    result[inResult] = deck[inDeck];
                    inDeck++;
                }
                b = !b;
            }
            inResult++;
        }
        return Solution.everyOther(deck, result, inDeck, b);
    }
}
