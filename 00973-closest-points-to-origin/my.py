from math import sqrt

class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = self.d)
        return points[:K]
        
    
    def d(self, point):
        return sqrt(point[0] * point[0] + point[1] * point[1])
