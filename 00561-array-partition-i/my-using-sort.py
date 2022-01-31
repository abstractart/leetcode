class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        r = 0
        for i in range(0, len(nums) - 1, 2):
            r += nums[i]
        
        return r
        
