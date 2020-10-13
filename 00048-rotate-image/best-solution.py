class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.swapRows(matrix)
        self.transpose(matrix)
        
        
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n - 1):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                
    def swapRows(self, matrix):
        top, bottom = 0, len(matrix) - 1
        
        while(top < bottom):
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            
            top += 1
            bottom -= 1
                
