class Solution {
    fun timeRequiredToBuy(tickets: IntArray, k: Int): Int {
        var ans = 0
        for (i in tickets.indices) {
            ans += if (i <= k) {
                kotlin.math.min(tickets[k], tickets[i])
            } else {
                kotlin.math.min(tickets[k] - 1, tickets[i])
            }
        }
        return ans
    }
}