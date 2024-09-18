class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = float('-inf')
        currSum = 0
        
        for x in nums:
            currSum = max(currSum +x, x)
            maxSum = max(maxSum, currSum)
            
        return maxSum