class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        
        m = len(matrix)
        if m == 0: return result
        
        n = len(matrix[0])
        
        pos = (0, 0)
        while(pos):
            result.append(matrix[pos[0]][pos[1]])
            pos = self.nextStep(pos, m, n)
            
        return result
    
    def nextStep(self, pos, m, n):
        if (pos[0] + pos[1]) % 2 == 0:
            if self.isUp(pos, m, n) and self.isRight(pos, m, n):
                return self.up(self.right(pos))
            elif self.isRight(pos, m, n):
                return self.right(pos)
            elif self.isDown(pos, m, n):
                return self.down(pos)
            
            return None
        else:
            
            if self.isDown(pos, m, n) and self.isLeft(pos, m, n):
                return self.down(self.left(pos))
            elif self.isDown(pos, m, n):
                return self.down(pos)
            elif self.isRight(pos, m, n):
                return self.right(pos)
            return None

        
        
    def isRight(self, pos, m, n):
        return pos[1] < n - 1
    
    def isUp(self, pos, m, n):
        return pos[0] > 0
    
    def isDown(self, pos, m, n):
        return pos[0] < m - 1
    
    def isLeft(self, pos, m, n):
        return pos[1] > 0
    
    def down(self, pos):
        return (pos[0] + 1, pos[1])
    
    def up(self, pos):
        return (pos[0] - 1, pos[1])
    
    def left(self, pos):
        return (pos[0], pos[1] - 1)
    
    def right(self, pos):
        return (pos[0], pos[1] + 1)
