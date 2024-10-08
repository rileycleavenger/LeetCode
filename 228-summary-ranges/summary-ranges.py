class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        res = []
        start = 0
        
        for end in range(1, len(nums)+1):
            if end == len(nums) or nums[end] != nums[end-1]+1:
                if start == end-1:
                    res.append(str(nums[start]))
                else:
                    res.append(str(nums[start])+"->"+str(nums[end-1]))
                start = end
        
        return res
            