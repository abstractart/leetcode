class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = nums[0]
        minVal = nums[0]
        
        result = nums[0]
        for i in range(1, len(nums)):
            newMax = max(minVal * nums[i], maxVal * nums[i], nums[i])
            newMin = min(minVal * nums[i], maxVal * nums[i], nums[i])
            
            maxVal, minVal = newMax, newMin
            result = max(result, maxVal)
            
            
            
        return result
