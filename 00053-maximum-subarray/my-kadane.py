class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]
        
        for i in range(1, len(nums)):
            currSum += nums[i]
            
            currSum = max(currSum, nums[i])
            maxSum = max(maxSum, currSum)
            
        return maxSum
