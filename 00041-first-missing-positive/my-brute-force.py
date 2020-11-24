class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 1
        if max(nums) <= 0: return 1
        
        s = set()
        for n in nums:
            s.add(n)
        
        for n in range(1, max(nums) + 2):
            if n not in s: return n
