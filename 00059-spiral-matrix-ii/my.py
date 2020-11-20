class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        steps = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        matrix = self.buildMatrix(n)
    
        i = j = 0
        left = 0
        right = n
        
        counter = 1
        
        while(left < right):
            for s in steps:
                count = right - left - 1
                if count == 0: count = 1
                for k in range(count):
                    if i not in range(left, right) or j not in range(left, right): break
                    
                    matrix[i][j] = counter
                    counter += 1
                    
                    i += s[0]
                    j += s[1]
            
            
            left += 1
            right -= 1
            
            i += 1
            j += 1                
        
        return matrix
        
    def buildMatrix(self, n: int) -> List[List[int]]:
        result = []
        
        for i in range(n):
            row = []
            for j in range(n):
                row.append(None)
            
            result.append(row)
                
        
        return result
        
