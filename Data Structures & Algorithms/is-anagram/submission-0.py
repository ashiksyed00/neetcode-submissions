class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # count the frequency of each charcter in 
        # both strings if they are same, return True
        # else False
        return Counter(s)==Counter(t)