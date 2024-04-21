class Solution {
    func makeGood(_ s: String) -> String {
        var stack = [Character]()
        for c in s {
            if stack.isEmpty {
                stack.append(c)
            } else {
                let last = stack.last!
                if last.isLowercase, last.uppercased() == String(c) {
                    stack.removeLast()
                } else if last.isUppercase, last.lowercased() == String(c) {
                    stack.removeLast()
                } else {
                    stack.append(c)
                }
            }
        }
        return String(stack)
    }
}
