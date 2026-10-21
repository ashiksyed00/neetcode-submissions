class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        add open par if open<n
        add closed only if closed<open
        if open==closed==n, add that to the result
        '''
        stack = []
        res = []

        def backtrack(openc, closedc):
            if openc==closedc==n:
                res.append("".join(stack))
                return
            
            if openc < n:
                stack.append('(')
                backtrack(openc + 1, closedc)
                stack.pop()
            
            if closedc < openc:
                stack.append(")")
                backtrack(openc, closedc + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

