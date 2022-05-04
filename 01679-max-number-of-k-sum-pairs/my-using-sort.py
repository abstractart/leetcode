class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        
        nums.sort()   
        left = 0
        right = len(nums) - 1
        
        while(left < right):
            s = nums[left] + nums[right]
            if s > k:
                right -= 1
            elif s < k:
                left += 1
            else:
                result += 1
                left += 1
                right -= 1
        
        return result
