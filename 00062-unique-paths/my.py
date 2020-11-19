class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = min(m, n), max(m, n)
        
        dp = []
        for i in range(1, m + 1):
            row = []
            for j in range(1, n + 1):
                if i == 1 or j == 1:
                    row.append(1)
                else:
                    row.append(row[-1] + dp[-1][j - 1])
            
            dp.append(row)
        
        return dp[-1][-1]
