class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.swapColumns(matrix)
        
        
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n - 1):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
    def swapColumns(self, matrix):
        n = len(matrix)
        for i in range(n):
            left, right = 0, n - 1
            
            while(left < right):
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                
                left += 1
                right -= 1
                
