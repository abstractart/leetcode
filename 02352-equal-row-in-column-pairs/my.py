from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c1 = self.getCounts(grid)
        self.transpose(grid)
        c2 = self.getCounts(grid)

        result = 0
        for r, count in c1.items():
            if r not in c2:
                continue
            result += c1[r] * c2[r]

        return result
    
    def transpose(self, grid):
        for i in range(len(grid)):
            for j in range(i + 1, len(grid)):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    
    def getCounts(self, grid):
        return Counter([tuple(row) for row in grid])
