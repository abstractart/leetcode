class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        currRowNegativeIndex = n - 1

        for row in grid:
            while currRowNegativeIndex >= 0 and row[currRowNegativeIndex] < 0:
                currRowNegativeIndex -= 1
            
            count += n - (currRowNegativeIndex + 1)
        
        return count
