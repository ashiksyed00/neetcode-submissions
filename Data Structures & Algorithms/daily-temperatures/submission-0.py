class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
           Use a monotonically decreasing stack to hold the temp
           store (temperatue, index) in the stack
           if current temperature is greater than the top of the 
           stack's temperature :
               store the current index - the top of the 
               stack index in the result
        '''

        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] <t:
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append([t, i])
        return res