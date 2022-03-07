from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums = sorted(set(nums))
    
        dp = [0] * (len(nums) + 2)
        
        dp[2] = nums[0] * counter[nums[0]]
    
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                dp[i + 2] = max(dp[i + 1], nums[i] * counter[nums[i]] + dp[i])
            else:
                dp[i + 2] = dp[i + 1] + nums[i] * counter[nums[i]]
                
        return dp[-1]
