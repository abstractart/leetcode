class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        acc = [[None for x in range(n)] for y in range(m)]
        
        acc[0][0] = 1
        self.helper(m - 1, n - 1, acc)

        return acc[-1][-1]
        
    def helper(self, m, n, acc):
        if m < 0 or n < 0: return 0
        if acc[m][n]: return acc[m][n]

        acc[m][n] = self.helper(m - 1, n, acc) + self.helper(m, n - 1, acc)

        return acc[m][n]
