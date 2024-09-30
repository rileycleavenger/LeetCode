class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        hash = {}
        
        for x in nums1:
            hash[x] = hash.get(x, 0) + 1
            
        for x in nums2:
            if x in hash and hash[x] > 0:
                hash[x] -= 1
                res.append(x)
                
        return res