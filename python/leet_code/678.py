class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        stars = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == '*':
                stars.append(i)
            else:
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
        while stack and stars:
            if stack[-1] > stars[-1]:
                return False
            stack.pop()
            stars.pop()
        return not stack
