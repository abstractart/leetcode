class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 1]
        
        if n in range(2):
            return dp[n]
        
        for i in range(2, n + 1):
            new = dp[-1] + dp[-2]
            
            dp[-2] = dp[-1]
            dp[-1] = new
            
        
        return dp[-1]
