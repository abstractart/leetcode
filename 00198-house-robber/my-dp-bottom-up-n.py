class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        
        for i in range(2, len(nums) + 2):
            dp[i] = max(nums[i - 2] + dp[i - 2], dp[i - 1])
        
        return dp[-1]
        
