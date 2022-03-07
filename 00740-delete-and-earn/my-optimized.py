from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums = sorted(set(nums))
    
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0] * counter[nums[0]]
    
        for i in range(1, len(nums)):
            points = nums[i] * counter[nums[i]]
            
            if nums[i] - nums[i - 1] == 1:
                dp[i + 1] = max(dp[i], dp[i - 1] + points)
            else:
                dp[i + 1] = dp[i] + points
                
        return dp[-1]
