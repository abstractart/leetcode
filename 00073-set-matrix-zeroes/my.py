class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 0: return
        
        m = len(matrix)
        n = len(matrix[0])

        cols = set()
        rows = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0: continue
                
                rows.add(i)
                cols.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0
