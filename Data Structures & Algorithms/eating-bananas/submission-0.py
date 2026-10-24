class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        We create an array from 0 to max(piles)
        then do binary search to check which 
        number gives the min eating speed
        '''

        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r)//2
            minh = 0
            for p in piles:
                minh += math.ceil(p/m)
            if minh <= h:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
        return res