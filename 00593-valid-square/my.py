from math import sqrt

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        points.sort()
        p1, p2, p3, p4 = points
        dist = [
            self.d(p1, p2),
            self.d(p1, p3),
            self.d(p2, p4),
            self.d(p3, p4)
        ]
        angles = [
            self.isAngle90(self.d(p1, p2), self.d(p1, p3), self.d(p2, p3)),
            self.isAngle90(self.d(p2, p4), self.d(p3, p4), self.d(p2, p3)),
            self.isAngle90(self.d(p1, p2), self.d(p2, p4), self.d(p1, p4)),
            self.isAngle90(self.d(p1, p3), self.d(p3, p4), self.d(p1, p4))
        ]
        
        print(points)
        print(dist)
        print(angles)
        return len(set(dist)) == 1 and dist[0] > 0 and len(set(angles)) == 1 and angles[0]
    
    def d(self, p1, p2):
        return pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)
    
    
    def isAngle90(self, a, b, c):
        # print(a, b, c, sqrt(a * a + b * b))
        return c == a + b
