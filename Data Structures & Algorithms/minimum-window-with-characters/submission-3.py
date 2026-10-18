class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""

        hashmapS, hashmapT = {}, {}

        for c in t:
            hashmapT[c] = hashmapT.get(c, 0) + 1

        match, need = 0, len(hashmapT)
        res, minLen = [-1,-1], len(s) + 2
        l=0
        for r in range(len(s)):
            hashmapS[s[r]] = hashmapS.get(s[r], 0) + 1
            if s[r] in hashmapT and hashmapS[s[r]] == hashmapT[s[r]]:
                match+=1
            
            while match == need:
                if (r-l+1)<minLen:
                    minLen = r-l+1
                    res = [l, r]
                
                hashmapS[s[l]]-=1
                if s[l] in hashmapT and hashmapS[s[l]] < hashmapT[s[l]]:
                    match-=1
                l+=1
        return s[res[0]:res[1]+1] if minLen!=len(s)+2 else ""
                

