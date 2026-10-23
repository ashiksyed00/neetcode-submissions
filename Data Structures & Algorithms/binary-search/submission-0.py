class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        mid = (low+high)//2
        if curr == target: return pos
        elif curr < target: low = mid + 1
        elif curr > target: high = mid -1
        '''

        l, h = 0, len(nums)-1
        while l<=h:
            mid = (l + h)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        return -1