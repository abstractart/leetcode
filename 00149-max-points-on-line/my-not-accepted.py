class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 2: return len(points)
        
        d = dict()
        result = 0
        for i in range(len(points) - 1):
            p = points[i]
            
            for j in range(i + 1, len(points)):
                q = points[j]
                if p == q: continue
                    
                coef = self.line(p, q)
                if coef not in d: d[coef] =  dict()
                    
                d[coef][(p[0], p[1])] = True
                d[coef][(q[0], q[1])] = True
                    
                if result < len(d[coef]): result = len(d[coef])
                    
        return result
                
        
    def line(self, p, q):
        x1, x2 = p[0], q[0]
        y1, y2 = p[1], q[1]
        
        if (x2 - x1) == 0: return (x1, None)
        if (y2 - y1) == 0: return (None, y1)

        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return m, b
