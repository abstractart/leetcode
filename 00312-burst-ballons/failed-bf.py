class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.append(1)
        nums.insert(0, 1)
        
        return self.helper(nums)
        
        
    def helper(self, nums):
        if len(nums) == 3: return nums[1]
    
        maximum = 0
        for i in range(1, len(nums) - 1):
            cp = list(nums)
            
            curr = self.coins(cp, i)
            cp.pop(i)
            
            val = self.helper(cp)
            
            if curr + val > maximum:
                maximum = curr + val
        
        return maximum
            
    
    def coins(self, nums, i):
        return nums[i - 1] * nums[i] * nums[i + 1]
