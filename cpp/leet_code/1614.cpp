// Optimizing the code for speed and unrolling loops for efficiency.
#pragma GCC optimize("O3,unroll-loops")
#include <string>

class Solution {
public:
    int maxDepth(std::string s) {
        int max_depth = 0;
        int depth = 0;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                depth++;
                max_depth = std::max(max_depth, depth);
            } else if (s[i] == ')') {
                depth--;
            }
        }
        return max_depth;
    }
};
