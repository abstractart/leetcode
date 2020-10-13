class Solution:
    def containsDuplicate(self, nums):
        counts = dict()
        
        for e in nums:
            counts[e] = counts.get(e, 0) + 1
            
            if counts[e] > 1: return True
            
        return False
        
