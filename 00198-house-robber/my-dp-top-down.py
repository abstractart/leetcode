class Solution:
    def rob(self, nums) -> int:
        return self.helper(nums, len(nums) - 1, [None] * len(nums))
    

    def helper(self, nums, n, dp):
        if n < 0:
            return 0     
        
        if dp[n] is None:
            dp[n] = max(
                self.helper(nums, n - 1, dp),
                self.helper(nums, n - 2, dp) +  nums[n],
            )
        
        return dp[n]
