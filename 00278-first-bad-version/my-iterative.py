class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        bad = None
    
        while(low <= high):
            m = low + (high - low) // 2
            if isBadVersion(m):
                bad = m
                high = m - 1
            else:
                low = m + 1
        
        return bad
