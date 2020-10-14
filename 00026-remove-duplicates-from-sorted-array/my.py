class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 0: return len(nums)
        
        n = len(nums)
        i = 1
        l = 1
        
        while(i < n):
            if nums[i] != nums[l - 1]:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
            
            i += 1
        return l
