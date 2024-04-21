class Solution {
    func minRemoveToMakeValid(_ s: String) -> String {
        var stack = [Int]()
        var s = Array(s)
        for i in 0 ..< s.count {
            if s[i] == "(" {
                stack.append(i)
            } else if s[i] == ")" {
                if stack.isEmpty {
                    s[i] = " "
                } else {
                    stack.removeLast()
                }
            }
        }
        for i in stack {
            s[i] = " "
        }
        return String(s.filter { $0 != " " })
    }
}
