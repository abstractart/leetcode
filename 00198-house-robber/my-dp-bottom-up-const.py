class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0, 0]
        
        for i in range(2, len(nums) + 2):
            new = max(nums[i - 2] + dp[-2], dp[-1])
            
            dp[-2] = dp[-1]
            dp[-1] = new
        
        return dp[-1]
