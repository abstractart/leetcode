class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        stack = []
        
        stack.append((0, len(nums) - 1))
        
        while(stack):
            start, stop = stack.pop()
            if start > stop:
                continue
            
            r = self.crossSubArraySum(nums, start, stop)
            result = max(result, r)
            
            middle = start + (stop - start) // 2
            stack.append((start, middle - 1))
            stack.append((middle + 1, stop))
            
        
        return result
    
    
    def crossSubArraySum(self, nums, start, stop):        
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
        
        return leftSum + nums[middle] + rightSum
