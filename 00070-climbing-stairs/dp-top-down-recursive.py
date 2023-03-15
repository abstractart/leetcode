class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n + 1)
        dp[0], dp[1] = 1, 1

        return self.helper(n, dp)

    
    def helper(self, n, dp):
        if not dp[n]:
            dp[n] = self.helper(n - 1, dp) + self.helper(n - 2, dp)
        
        return dp[n]
