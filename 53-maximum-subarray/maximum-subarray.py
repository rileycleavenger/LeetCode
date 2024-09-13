class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = 0
        maxSum = float('-inf')
        
        for x in nums:
            currSum = max(x+currSum, x)
            maxSum = max(maxSum, currSum)
            
        return maxSum