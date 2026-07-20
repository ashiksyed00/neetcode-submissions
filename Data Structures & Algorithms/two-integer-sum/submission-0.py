class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use as hashmap to store the compliment of the current number
        # Algorithm
        # Traverse the array and for each number check if it's compliment 
        # is present in the hashmap if yes return indices

        compliment = {}
        for i in range(len(nums)):
            if nums[i] not in compliment:
                compliment[target - nums[i]] = i
            else:
                return [compliment[nums[i]], i]