class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = []
        if n >= 0: nums.append(0)
        if n >= 1: nums.append(1) 
        
        for k in range(2, n + 1):
            if k % 2 == 0:
                nums.append(nums[k // 2])
            else:
                i = (k - 1) // 2
                nums.append(nums[i] + nums[i + 1])
        
        return max(nums)
