from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums = sorted(set(nums))
        result = 0
        
        
        for s in self.splitSubArrays(nums):
            result += self.getValue(s, counter)
            
        return result

    def splitSubArrays(self, nums):
        subarrays = []
        i = 0
        while(i < len(nums)):
            j = i
            while(j + 1 < len(nums) and nums[j + 1] - nums[j] <= 1):
                j += 1

            subarrays.append(nums[i:(j + 1)])
            
            i = j + 1
        return subarrays
    
        
            
    
    def getValue(self, nums, counter):
        dp = [0] * (len(nums) + 2)
        
        for i in range(len(nums)):
            dp[i + 2] = max(dp[i + 1], dp[i] + nums[i] * counter[nums[i]])
        
        return dp[-1]
