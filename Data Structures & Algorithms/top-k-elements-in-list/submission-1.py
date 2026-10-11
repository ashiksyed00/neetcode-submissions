class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 

        for n in nums:
            count[n] = count.get(n,0)+1
        # {1:1,2:2,3:3}

        buckets = [[] for _ in range(len(nums)+1)] # [[],[],[],[],[],[],[]]
        for n,c in count.items():
            print(n,c)
            buckets[c].append(n)
        # [[],[1],[2],[3],[],[],[]]
        res=[]
        for i in range(len(nums),-1,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res)==k:
                    return res
            

