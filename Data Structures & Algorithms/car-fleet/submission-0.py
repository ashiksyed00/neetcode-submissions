class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Traverse in the reverse order of position
        calculate the time taken to reach the destination for
        the car from it's position
        time = (target - i)/speed
        push the value to the stack
        if current time is less than the stack top speed:
            pop the stack and replace with current values
        
        """

        stack = []
        pair = [(p,s) for p,s in zip(position, speed)]

        for p,s in sorted(pair, reverse=True):
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        