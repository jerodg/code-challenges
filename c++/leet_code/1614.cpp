class Solution {
public:
    int maxDepth(string s) {
        int max_depth = 0;
        int depth = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                depth++;
                max_depth = max(max_depth, depth);
            } else if (s[i] == ')') {
                depth--;
            }
        }
        return max_depth;
    }
};