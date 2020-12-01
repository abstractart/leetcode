class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = min(m, n), max(m, n)
        
        dp = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(None)
            
            dp.append(row)
            
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                    continue
                
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[m - 1][n - 1]
