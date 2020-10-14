class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        l = 1
        
        for i in range(len(nums)):
            if nums[i] == nums[l - 1]: continue
            
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
        
        return l
