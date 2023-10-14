class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.helper(nums, 0, len(nums) - 1)
    
    
    def helper(self, nums, start, stop):
        if start > stop:
            return float("-inf")
        
        middle = start + (stop - start) // 2
        
        leftSum, currLeftSum = 0, 0
        rightSum, currRightSum = 0, 0
        
        left, right = middle - 1, middle + 1
        while(left >= start):
            currLeftSum += nums[left]
            leftSum = max(leftSum, currLeftSum)
            left -= 1

        while(right <= stop):
            currRightSum += nums[right]
            rightSum = max(rightSum, currRightSum)
            right += 1
        
        return max(
            leftSum + nums[middle] + rightSum,
            self.helper(nums, start, middle - 1),
            self.helper(nums, middle + 1, stop)
        )
