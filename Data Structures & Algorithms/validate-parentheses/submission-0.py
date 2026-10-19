class Solution:
    def isValid(self, s: str) -> bool:
        parpair = {'}':'{', ')':'(',']':'['}
        stack = []
        for c in s:
            if c in parpair:
                if stack and stack[-1]==parpair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False