class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hash = {}
        
        for x in nums:
            hash[x] = hash.get(x, 0) + 1
            if x in hash and hash[x] > 1:
                return True
            
        
        return False