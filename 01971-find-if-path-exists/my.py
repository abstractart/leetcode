class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        matr = self.buildMatr(n, edges)
        return self.findPath(matr, source, destination)
        
    
    def findPath(self, matr, source, dest):        
        stack = [source]
        visited = set()
    
        while(stack):
            curr = stack.pop()
            
            if curr == dest:
                return True
            
            for edge in matr[curr]:
                if edge not in visited:
                  stack.append(edge)
            
            visited.add(curr)
        
        return False
            
    
    def buildMatr(self, n, edges):
        matr = [set() for _ in range(n)]            
        for e in edges:
            matr[e[0]].add(e[1])
            matr[e[1]].add(e[0])
        
        return matr
