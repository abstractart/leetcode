class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        l = 1
        for i in range(len(nums)):
            if nums[i] == nums[l - 1]: continue
            
            nums[l] = nums[i]
            l += 1
        
        return l
