class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        nums.sort()
        
        result = 1
        lcc = 1
        
        i = 0
        while(i < len(nums) - 1):            
            if nums[i + 1] - nums[i] > 1:
                lcc = 1
            elif nums[i + 1] - nums[i] == 1:
                lcc += 1
            
            result = max(lcc, result)
            i += 1
                
            

        return result
