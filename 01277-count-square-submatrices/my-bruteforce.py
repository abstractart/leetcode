class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        return self.bruteforce(matrix)
    
    
    def bruteforce(self, matrix):
        m, n = len(matrix), len(matrix[0])
        count = 0
        
        for size in range(1, min(m, n) + 1):
            for row in range(m - size + 1):
                for column in range(n - size + 1):
                    if self.isAllOnes(matrix, row, column, size):
                        count += 1
        
        return count
    
    def isAllOnes(self, matrix, row, column, size):
        for row_nest in range(row, row + size):
            for column_nest in range(column, column + size):
                if not matrix[row_nest][column_nest]:
                    return False
        
        return True
