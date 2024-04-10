import java.util.*

class Solution {
    fun deckRevealedIncreasing(deck: IntArray): IntArray {
        val N = deck.size
        val result = IntArray(N)

        Arrays.sort(deck)

        return everyOther(deck, result, 0, 0, false)
    }

    private tailrec fun everyOther(
        deck: IntArray,
        result: IntArray,
        indexInDeck: Int,
        indexInResult: Int,
        skip: Boolean
    ): IntArray {
        val N = deck.size

        if (indexInDeck == N) {
            return result
        }

        var newIndexInDeck = indexInDeck
        var newIndexInResult = indexInResult
        var newSkip = skip

        while (newIndexInResult < N) {
            if (result[newIndexInResult] == 0) {
                if (!newSkip) {
                    result[newIndexInResult] = deck[newIndexInDeck]
                    newIndexInDeck++
                }
                newSkip = !newSkip
            }
            newIndexInResult++
        }

        return everyOther(deck, result, newIndexInDeck, 0, newSkip)
    }
}