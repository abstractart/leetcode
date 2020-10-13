class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        zeroIndex = 0 # Last zero
        nonZeroIndex = zeroIndex # Current
        
        while(nonZeroIndex < len(nums)):
            if nums[nonZeroIndex] != 0:
                    nums[zeroIndex], nums[nonZeroIndex] = nums[nonZeroIndex], nums[zeroIndex]
                    zeroIndex += 1
                
            nonZeroIndex += 1
        
