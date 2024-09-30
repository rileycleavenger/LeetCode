class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash = {}
        
        for x in s:
            hash[x] = hash.get(x, 0) + 1
            
        for x in t:
            hash[x] = hash.get(x, 0) - 1
            
        for x in hash:
            if hash[x] != 0: return x
            
        return 0