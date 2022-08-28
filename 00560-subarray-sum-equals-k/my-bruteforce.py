class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            s = 0
            
            for j in range(i, len(nums)):
                s += nums[j]
                if s == k:
                    result += 1
        
        return result
