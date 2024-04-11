import java.util.Arrays;

public class Solution {
  public int[] deckRevealedIncreasing(final int[] deck) {
    final int N = deck.length;
    final int[] result = new int[N];

    Arrays.sort(deck);

    return this.everyOther(deck, result, 0, 0, false);
  }

  private int[] everyOther(
      final int[] deck, final int[] result, int indexInDeck, int indexInResult, boolean skip) {
    final int N = deck.length;

    if (indexInDeck == N) {
      return result;
    }

    while (indexInResult < N) {
      if (0 == result[indexInResult]) {
        if (!skip) {
          result[indexInResult] = deck[indexInDeck];
          indexInDeck++;
        }
        skip = !skip;
      }
      indexInResult++;
    }

    return this.everyOther(deck, result, indexInDeck, 0, skip);
  }
}
