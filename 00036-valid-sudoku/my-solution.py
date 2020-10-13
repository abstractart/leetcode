from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validRows(board) and self.validColumns(board) and self.validBoxes(board)
    
    
    def validRows(self, board):
        for row in board:
            val = self.validRow(row)
            if not val: return False
        
        return True

    
    def validRow(self, row):
        counts = Counter(row)
        for k in counts.keys():
            if k == ".": continue
            if counts[k] > 1: return False
        
        return True
    
    def validColumns(self, board):
        for i in range(len(board)):
            column = []
            for j in range(len(board)):
                column.append(board[j][i])
                
            val = self.validRow(column)
            if not val: return False
            
            
        return True
    
    def validBoxes(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                val = self.validBox(board, i, j)
                
                if not val: return False
        return True
    
    def validBox(self, board, row, column):
        values = []
        
        for i in range(row, row + 3):
            for j in range(column, column + 3):
                values.append(board[i][j])
            
        return self.validRow(values)
