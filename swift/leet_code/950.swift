import Foundation

class Solution {
    func deckRevealedIncreasing(_ deck: [Int]) -> [Int] {
        let n = deck.count
        var sortedDeck = deck.sorted()
        var q: [Int] = Array(0..<n)
        var ans = [Int](repeating: 0, count: n)

        for i in 0..<n {
            let idx = q.removeFirst()
            if !q.isEmpty {
                q.append(q.removeFirst())
            }
            ans[idx] = sortedDeck[i]
        }
        return ans
    }
}
