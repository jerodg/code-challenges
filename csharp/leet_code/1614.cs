public class Solution {
    public int MaxDepth(string s) {
        int maxDepth = 0;
        int currentDepth = 0;
        foreach(char c in s) {
            if(c == '(') {
                currentDepth++;
                maxDepth = Math.Max(maxDepth, currentDepth);
            } else if(c == ')') {
                currentDepth--;
            }
        }
        return maxDepth;
    }
}