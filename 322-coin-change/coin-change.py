class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+10]*(amount+1)
        dp[0] = 0
        
        for a in range(amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
                    
        if dp[amount] == amount+10:
            return -1
        else:
            return dp[amount]