class Solution {
    func maxDepth(_ s: String) -> Int {
        var maxDepth = 0
        var depth = 0
        for char in s {
            if char == "(" {
                depth += 1
            } else if char == ")" {
                depth -= 1
            }
            maxDepth = max(maxDepth, depth)
        }
        return maxDepth
    }
}
