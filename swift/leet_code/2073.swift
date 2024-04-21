class Solution {
    func timeRequiredToBuy(_ tickets: [Int], _ k: Int) -> Int {
        var result = 0
        var tickets = tickets
        let count = tickets.count

        while tickets[k] != 0 {
            for i in 0 ..< count {
                if tickets[i] != 0 {
                    tickets[i] -= 1
                    result += 1

                    if tickets[k] == 0 { return result }
                }
            }
        }
        return result
    }
}
