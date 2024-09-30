class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}
        res = set()
        
        for x in nums1:
            hash[x] = hash.get(x, 0) + 1
            
        for x in nums2:
            if x in hash:
                res.add(x)
                
        return res