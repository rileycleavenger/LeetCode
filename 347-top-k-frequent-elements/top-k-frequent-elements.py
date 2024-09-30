class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash = {}
        
        for x in nums:
            hash[x] = hash.get(x, 0) + 1
            
        sorted_hash = sorted(hash.items(), key=lambda item: item[1], reverse=True)
        
        res = []
        for x in sorted_hash:
            res.append(x[0])
            if len(res) == k:
                return res
        
        return []