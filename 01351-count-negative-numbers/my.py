class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()

        stack = []

        stack.append((m - 1, n - 1))
        visited.add((m - 1, n - 1))

        r = 0
        while(stack):
            i, j = stack.pop()
            if not grid[i][j] < 0:
                continue
            
            r += 1
            candidateUp = (i - 1, j)
            if candidateUp[0] in range(m) and candidateUp not in visited:
                stack.append(candidateUp)
                visited.add(candidateUp)     
            
            candidateLeft = (i, j - 1)
            if candidateLeft[1] in range(n) and candidateLeft not in visited:
                stack.append(candidateLeft)
                visited.add(candidateLeft)
        
        return r
