class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longSeq = 0

        for n in nums:
            if (n-1) not in numSet:
                currlong = 0
                i = n
                while i in numSet:
                    currlong+=1
                    i+=1
                longSeq = max(longSeq, currlong)
        return longSeq
