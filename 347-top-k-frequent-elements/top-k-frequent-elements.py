from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        hash_map = {}
        
        for x in nums:
            hash_map[x] = hash_map.get(x, 0) + 1
        
        # Step 2: Sort the items based on frequency
        # `sorted` returns a list of tuples (key, value)
        sorted_items = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)
        
        # Step 3: Collect the top k frequent elements
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])  # Append the key (the number)

        return res
