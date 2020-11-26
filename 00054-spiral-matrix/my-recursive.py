class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return self.spiralOrderRec(matrix, [0, len(matrix) - 1], [0, len(matrix[0]) -1], [])
    
    def spiralOrderRec(self, matrix, rows, columns, acc):
        if rows[0] > rows[1] or columns[0] > columns[1]: return acc
                
        curr = [rows[0], columns[0]]
        while(True):
            acc.append(matrix[curr[0]][curr[1]])
            
            next_step = self.nextStep(curr, rows, columns)
            if not next_step: break
            
            curr = [
                curr[0] + next_step[0], 
                curr[1] + next_step[1]
            ]
            if curr == [rows[0], columns[0]]: break
        
        return self.spiralOrderRec(matrix, [rows[0] + 1, rows[1] - 1], [columns[0] + 1, columns[1] -1], acc)
    
    
    def allowRight(self, curr, rows, columns):
        return curr[1] < columns[1] and curr[0] == rows[0]
    
    def allowDown(self, curr, rows, columns):
        return curr[0] < rows[1] and curr[1] == columns[1]
    
    def allowLeft(self, curr, rows, columns):
        if rows[0] == rows[1]: return False
        return curr[1] > columns[0] and curr[0] == rows[1]
    
    def allowUp(self, curr, rows, columns):
        if columns[0] == columns[1]: return False
        return curr[0] > rows[0] and curr[1] == columns[0]
    
    def nextStep(self, curr, rows, columns):
        if self.allowRight(curr, rows, columns): return [0, 1]
        if self.allowDown(curr, rows, columns): return [1, 0]
        if self.allowLeft(curr, rows, columns): return [0, -1]
        if self.allowUp(curr, rows, columns): return [-1, 0]
