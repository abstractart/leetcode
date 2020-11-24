class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        
        firstMissing = 1
        for n in nums:
            if n <= 0: continue
            
            if n > firstMissing: return firstMissing
            if n == firstMissing: firstMissing += 1
        
        return firstMissing
