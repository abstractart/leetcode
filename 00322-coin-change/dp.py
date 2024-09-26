class Solution:
    def coinChange(self, coins, amount):
        coins.sort(reverse = True)
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
                    
        if dp[-1] == float("inf"):
            return -1
        
        return dp[-1]
            
        
        
