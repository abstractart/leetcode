class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = dict()        
        circles = 0
        
        for i in range(n):
            if visited.get(i): continue
            
            stack = [(i, i)]
            while(len(stack) > 0):
                i, j = stack.pop()
                
                for index in range(n):
                    if visited.get(index): continue
                    if M[i][index]: stack.append((i, index))  
                    if M[index][j]: stack.append((j, index))   
                
                visited[i] = True
                visited[j] = True
 
            circles += 1
            
        return circles
