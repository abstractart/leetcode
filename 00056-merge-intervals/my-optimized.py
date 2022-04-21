class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        
        for i in intervals:
            self.isOverLapping(result, i)
        
        
        return result
    
    def isOverLapping(self, intervals, interval):
        if intervals and self.overlaps(intervals[-1], interval):
            intervals[-1][0] = min(intervals[-1][0], interval[0])
            intervals[-1][1] = max(intervals[-1][1], interval[1])
            return
        
        intervals.append([interval[0], interval[1]])
    
    def overlaps(self, i1, i2):
        if i1[0] > i2[0]: i1, i2 = i2, i1
        
        return i2[0] in range(i1[0], i1[1] + 1)
