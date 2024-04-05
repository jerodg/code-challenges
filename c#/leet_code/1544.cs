public class Solution {
    public string MakeGood(string s) {
        Stack<char> stack = new Stack<char>();
        foreach (char c in s) {
            if (stack.Count > 0 && Math.Abs(stack.Peek() - c) == 32) {
                stack.Pop();
            } else {
                stack.Push(c);
            }
        }
        char[] result = stack.ToArray();
        Array.Reverse(result);
        return new string(result);
    }
}