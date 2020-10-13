# Thanks Nick White https://www.youtube.com/watch?v=Pl7mMcBm2b8
from collections import Counter

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                value = board[i][j]
                
                column = "{}-column-{}".format(value, j)
                row = "{}-row-{}".format(value, i)
                box = "{}-board-{}-{}".format(value, i // 3, j // 3)
                
                if column in seen or row in seen or box in seen: return False
                
                seen.add(column)
                seen.add(row)
                seen.add(box)
        
        return True
