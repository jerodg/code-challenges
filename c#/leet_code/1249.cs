public class Solution {
    public string MinRemoveToMakeValid(string s) {
        Stack<int> stack = new Stack<int>();
        HashSet<int> toRemove = new HashSet<int>();
        for (int i = 0; i < s.Length; i++) {
            if (s[i] == '(') {
                stack.Push(i);
            } else if (s[i] == ')') {
                if (stack.Count == 0) {
                    toRemove.Add(i);
                } else {
                    stack.Pop();
                }
            }
        }
        while (stack.Count > 0) {
            toRemove.Add(stack.Pop());
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.Length; i++) {
            if (!toRemove.Contains(i)) {
                sb.Append(s[i]);
            }
        }
        return sb.ToString();
    }
}