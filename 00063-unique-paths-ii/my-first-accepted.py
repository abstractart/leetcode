class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[None for x in range(n)] for y in range(m)]
        if obstacleGrid[0][0]:
            dp[0][0] = 0
        else:
            dp[0][0] = 1 
        for i in range(1, n):
            if not obstacleGrid[0][i]:
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = 0
        
        for i in range(1, m):
            if not obstacleGrid[i][0]:
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = 0
        
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[-1][-1]
