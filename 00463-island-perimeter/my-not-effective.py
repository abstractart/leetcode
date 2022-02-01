class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        result = 0
        
        for i in range(row):
            for j in range(col):
                if not grid[i][j]: continue
                
                perimeter = 0
                if i == 0:
                    perimeter += 1
                if i == row - 1:
                    perimeter += 1
                
                if j == 0:
                    perimeter += 1
                
                if j == col - 1:
                    perimeter += 1
                
                
                if j + 1 in range(col) and not grid[i][j + 1]:
                    perimeter += 1
                
                if j - 1 in range(col) and not grid[i][j - 1]:
                    perimeter += 1
                
                if i - 1 in range(row) and not grid[i - 1][j]:
                    perimeter += 1
                
                if i + 1 in range(row) and not grid[i + 1][j]:
                    perimeter += 1
                    
                result += perimeter
                    
                
        return result
            
