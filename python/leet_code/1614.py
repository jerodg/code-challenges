class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1
        return max_depth
