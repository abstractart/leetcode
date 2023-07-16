class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m == 1 or n == 1:
            return mat
        
        # each column
        for j in range(n):
            self.sort(mat, 0, j, m, n)
        
        # each row
        for i in range(m):
            self.sort(mat, i, 0,  m, n)
        
        return mat
    
    
    def sort(self, mat, i, j, m, n):
        values = []
        
        # loop through diagonal
        while(i < m and j < n):
            values.append(mat[i][j])
            
            i += 1
            j += 1
        
        values.sort()
        
        # substract because i and j out of range
        i -= 1
        j -= 1

        # fill diagonal in reversed order
        while(values):
            mat[i][j] = values.pop()
            i -= 1
            j -= 1 
